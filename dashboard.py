from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from run_pipeline import run_pipeline
import re

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
app.title = "Pharma Executive Intelligence"

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


app.layout = dbc.Container([

    dbc.Row([
        dbc.Col(html.H1("Pharma Executive Intelligence Dashboard",
                        className="text-center text-primary my-4"))
    ]),

    dbc.Row([
        dbc.Col(dbc.Button("Run Intelligence Engine",
                           id="run-btn",
                           color="warning",
                           className="mb-4"), width="auto")
    ]),

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

    dbc.Row([
        dbc.Col(dcc.Graph(id="risk-gauge"))
    ])

], fluid=True)


@app.callback(
    Output("market-condition", "children"),
    Output("top-priority", "children"),
    Output("risk-level", "children"),
    Output("exec-action", "children"),
    Output("risk-gauge", "figure"),
    Input("run-btn", "n_clicks")
)
def update_dashboard(n):

    if not n:
        return "", "", "", "", {}

    outputs = run_pipeline()
    supervisor_text = outputs["supervisor"]

    parsed = parse_supervisor(supervisor_text)

    # Risk numeric mapping
    risk_map = {"Low": 1, "Medium": 2, "High": 3}
    risk_value = risk_map.get(parsed["risk"], 0)

    # Gauge Chart
    fig = go.Figure(go.Indicator(
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

    return (
        parsed["market"],
        parsed["priority"],
        parsed["risk"],
        parsed["action"],
        fig
    )


if __name__ == "__main__":
    app.run(debug=True)
