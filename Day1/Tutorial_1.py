import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


Data = [2, 5, 3]
Title = "Native Plotly rendering in Dash"
Labels = ['Mumbai','Nagpur','Delhi']
fig = go.Figure(
    data=[go.Bar(y=Data, x=Labels)],
    layout_title_text=Title
)

print(fig)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
])

app.run_server(debug=True)