from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from run_pipeline import run_pipeline
import pandas as pd
import re

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
app.title = "Pharma Executive Intelligence"


# parser supervisor agent ke ouptut ke liye

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
        parts = c.split(",")
        for p in parts:
            company_list.append(p.strip())

    company_df = pd.DataFrame({"Company": company_list})
    company_count = company_df["Company"].value_counts().reset_index()
    company_count.columns = ["Company", "Count"]

    therapy_df = pd.DataFrame({"Therapy": therapies})
    therapy_count = therapy_df["Therapy"].value_counts().reset_index()
    therapy_count.columns = ["Therapy", "Count"]

    return company_count, therapy_count


#layout

app.layout = dbc.Container([

    dbc.Row([
        dbc.Col(html.H1("Pharma Executive Intelligence Dashboard",
                        className="text-center text-info my-4"))
    ]),

    dbc.Row([
        dbc.Col(dbc.Button("Run Intelligence Engine",
                           id="run-btn",
                           color="warning",
                           className="mb-4"), width="auto")
    ]),

    # Executive Cards
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Overall Market Condition"),
            dbc.CardBody(html.P(id="market-condition"))
        ], color="dark", inverse=True), width=6),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Top Strategic Priority"),
            dbc.CardBody(html.P(id="top-priority"))
        ], color="danger", inverse=True), width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Risk Concentration"),
            dbc.CardBody(html.H3(id="risk-level",
                                 className="text-center"))
        ], color="warning", inverse=True), width=4),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Immediate Executive Action"),
            dbc.CardBody(html.P(id="exec-action"))
        ], color="success", inverse=True), width=8)
    ], className="mb-4"),

    # Graphs Row 1
    dbc.Row([
        dbc.Col(dcc.Graph(id="risk-gauge"), width=6),
        dbc.Col(dcc.Graph(id="signal-pie"), width=6)
    ], className="mb-4"),

    # Graphs Row 2
    dbc.Row([
        dbc.Col(dcc.Graph(id="company-bar"), width=6),
        dbc.Col(dcc.Graph(id="therapy-bar"), width=6)
    ])

], fluid=True)


#ckallback system

@app.callback(
    Output("market-condition", "children"),
    Output("top-priority", "children"),
    Output("risk-level", "children"),
    Output("exec-action", "children"),
    Output("risk-gauge", "figure"),
    Output("signal-pie", "figure"),
    Output("company-bar", "figure"),
    Output("therapy-bar", "figure"),
    Input("run-btn", "n_clicks")
)
def update_dashboard(n):

    if not n:
        return "", "", "", "", {}, {}, {}, {}

    outputs = run_pipeline()

    supervisor_text = outputs["supervisor"]
    signal_text = outputs["signal"]
    scout_text = outputs["scout"]

    parsed = parse_supervisor(supervisor_text)

    # Risk numeric mapping
    risk_map = {"Low": 1, "Medium": 2, "High": 3}
    risk_text = parsed["risk"].strip().lower()
    

    if "high" in risk_text:
        risk_value = 3
    elif "medium" in risk_text:
        risk_value = 2
    elif "low" in risk_text:
        risk_value = 1
    else:
        risk_value = 0

    # Gauge
    gauge_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_value,
        gauge={
            "axis": {"range": [0, 3]},
            "steps": [
                {"range": [0, 1], "color": "green"},
                {"range": [1, 2], "color": "yellow"},
                {"range": [2, 3], "color": "red"}
            ]
        },
        title={"text": "Market Risk Index"}
    ))

    # Signal Pie
    signal_df = parse_signals(signal_text)
    signal_fig = px.pie(
        signal_df,
        names="Signal",
        values="Count",
        title="Strategic Signal Distribution"
    )

    # Company & Therapy Charts
    company_df, therapy_df = parse_scout_data(scout_text)

    company_fig = px.bar(
        company_df,
        x="Company",
        y="Count",
        title="Company Activity Frequency"
    )

    therapy_fig = px.bar(
        therapy_df,
        x="Therapy",
        y="Count",
        title="Therapy Area Distribution"
    )

    return (
        parsed["market"],
        parsed["priority"],
        parsed["risk"],
        parsed["action"],
        gauge_fig,
        signal_fig,
        company_fig,
        therapy_fig
    )


if __name__ == "__main__":
    app.run(debug=True)
