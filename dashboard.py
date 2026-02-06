from dash import Dash, html, dcc, Input, Output, State,callback_context
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from run_pipeline import run_pipeline
import pandas as pd
import re
import time

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Pharma Executive Intelligence"


# =========================
# PARSERS
# =========================

def parse_supervisor(text):
    market = re.search(r"Overall Market Condition:(.*?)(🚨|Top Strategic Priority:)", text, re.S)
    priority = re.search(r"Top Strategic Priority:(.*?)(📊|Risk Concentration:)", text, re.S)
    risk = re.search(r"Risk Concentration:(.*?)(🎯|Immediate Executive Action:)", text, re.S)
    action = re.search(r"Immediate Executive Action:(.*)", text, re.S)

    return {
        "market": market.group(1).strip() if market else "Not Available",
        "priority": priority.group(1).strip() if priority else "Not Available",
        "risk": risk.group(1).strip() if risk else "Unknown",
        "action": action.group(1).strip() if action else "Not Available"
    }


def parse_signals(text):
    categories = [
        "Competitive Threat",
        "Market Opportunity",
        "Pricing Shift",
        "Regulatory Risk",
        "Brand Momentum"
    ]
    counts = {c: text.count(c) for c in categories}

    return pd.DataFrame({
        "Signal": list(counts.keys()),
        "Count": list(counts.values())
    })


def parse_scout_data(text):
    companies = re.findall(r"Companies Involved:(.*)", text)
    therapies = re.findall(r"Therapy Area:(.*)", text)

    company_list = []
    for c in companies:
        for p in c.split(","):
            company_list.append(p.strip())

    company_df = pd.DataFrame({"Company": company_list})
    company_count = company_df["Company"].value_counts().reset_index()
    company_count.columns = ["Company", "Count"]

    therapy_df = pd.DataFrame({"Therapy": therapies})
    therapy_count = therapy_df["Therapy"].value_counts().reset_index()
    therapy_count.columns = ["Therapy", "Count"]

    return company_count, therapy_count


# =========================
# LAYOUT
# =========================

app.layout = dbc.Container([

    dcc.Interval(id="auto-refresh", interval=60*1000, n_intervals=0),

    html.H1(
        "🚀 Pharma Intelligence War Room",
        style={
            "textAlign": "center",
            "fontSize": "36px",
            "fontWeight": "bold",
            "marginBottom": "20px",
            "color": "#00F5FF"
        }
    ),

    dbc.Row([
        dbc.Col(
            dbc.Button("🔄 Refresh Now",
                       id="refresh-now",
                       color="warning",
                       size="lg"),
            width="auto"
        ),
        dbc.Col(
            html.Div(id="refresh-status",
                     style={"marginTop": "10px", "color": "#00F5FF"}),
            width="auto"
        )
    ], className="mb-4"),

    # Executive Cards
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("🌍 Overall Market Condition"),
            dbc.CardBody(html.P(id="market-condition"))
        ]), width=6),

        dbc.Col(dbc.Card([
            dbc.CardHeader("🔥 Top Strategic Priority"),
            dbc.CardBody(html.P(id="top-priority"))
        ], color="danger", inverse=True), width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("⚠ Risk Concentration"),
            dbc.CardBody(html.H3(id="risk-level",
                                 className="text-center"))
        ], color="warning", inverse=True), width=4),

        dbc.Col(dbc.Card([
            dbc.CardHeader("🎯 Immediate Executive Action"),
            dbc.CardBody(html.P(id="exec-action"))
        ], color="success", inverse=True), width=8)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id="risk-gauge"), width=6),
        dbc.Col(dcc.Graph(id="signal-pie"), width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id="company-bar"), width=6),
        dbc.Col(dcc.Graph(id="therapy-bar"), width=6)
    ])

], fluid=True)


# =========================
# CALLBACK
# =========================

@app.callback(
    Output("market-condition", "children"),
    Output("top-priority", "children"),
    Output("risk-level", "children"),
    Output("exec-action", "children"),
    Output("risk-gauge", "figure"),
    Output("signal-pie", "figure"),
    Output("company-bar", "figure"),
    Output("therapy-bar", "figure"),
    Output("refresh-status", "children"),
    Input("auto-refresh", "n_intervals"),
    Input("refresh-now", "n_clicks"),
    prevent_initial_call=True
)
def update_dashboard(n_intervals, refresh_click):

    ctx = callback_context
    force_refresh = False

    if ctx.triggered and ctx.triggered[0]["prop_id"].startswith("refresh-now"):
        force_refresh = True

    outputs = run_pipeline(force=force_refresh)

    parsed = parse_supervisor(outputs["supervisor"])
    signal_df = parse_signals(outputs["signal"])
    company_df, therapy_df = parse_scout_data(outputs["scout"])

    risk_text = parsed["risk"].lower()

    if "high" in risk_text:
        risk_value = 3
    elif "medium" in risk_text:
        risk_value = 2
    elif "low" in risk_text:
        risk_value = 1
    else:
        risk_value = 0

    gauge_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_value,
        gauge={
            "axis": {"range": [0, 3]},
            "bar": {"color": "#00F5FF"}
        }
    ))

    signal_fig = px.pie(signal_df, names="Signal", values="Count")

    company_fig = px.bar(company_df, x="Company", y="Count")

    therapy_fig = px.bar(therapy_df, x="Therapy", y="Count")

    status_text = f"Last Updated: {time.strftime('%H:%M:%S')}"

    return (
        parsed["market"],
        parsed["priority"],
        parsed["risk"],
        parsed["action"],
        gauge_fig,
        signal_fig,
        company_fig,
        therapy_fig,
        status_text
    )


if __name__ == "__main__":
    app.run(debug=True)
