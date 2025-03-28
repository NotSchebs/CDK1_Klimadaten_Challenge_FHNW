import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Beispiel-Daten
df = pd.DataFrame({
    "Jahr": [2018, 2019, 2020, 2021, 2022],
    "Produktion (GWh)": [5000, 5200, 5400, 5300, 5500]
})

fig = px.line(df, x="Jahr", y="Produktion (GWh)", title="Stromproduktion über die Jahre")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Atomkraft-Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
