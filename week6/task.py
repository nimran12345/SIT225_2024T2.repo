import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load Data with proper date parsing
try:
    df = pd.read_csv("gyroscope_data (3).csv", parse_dates=True, infer_datetime_format=True)
except FileNotFoundError:
    print("Error: The file 'gyroscope_data.csv' was not found. Ensure it's in the correct directory.")
    exit()

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Gyroscope Data Dashboard", style={'textAlign': 'center'}),

    # Dropdown for selecting graph type
    html.Label("Select Graph Type:"),
    dcc.Dropdown(
        id='graph-type',
        options=[
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Distribution Plot', 'value': 'hist'}
        ],
        value='line',
        clearable=False
    ),

    # Dropdown for selecting variables
    html.Label("Select Data Variables (x, y, z):"),
    dcc.Dropdown(
        id='variable-selector',
        options=[
            {'label': 'X-Axis', 'value': 'x'},
            {'label': 'Y-Axis', 'value': 'y'},
            {'label': 'Z-Axis', 'value': 'z'}
        ],
        value=['x', 'y', 'z'],
        multi=True
    ),

    # Input for number of data samples
    html.Label("Number of Samples:"),
    dcc.Input(id="num-samples", type="number", value=100, min=10, step=10),

    # Buttons for navigating dataset
    html.Button("Previous", id="prev-btn", n_clicks=0),
    html.Button("Next", id="next-btn", n_clicks=0),

    # Graph Output
    dcc.Graph(id="gyro-graph"),

    # Data Summary Table
    html.H3("Data Summary"),
    html.Div(id="data-summary")
])

# Callback to update the graph
@app.callback(
    Output("gyro-graph", "figure"),
    Output("data-summary", "children"),
    Input("graph-type", "value"),
    Input("variable-selector", "value"),
    Input("num-samples", "value"),
    Input("prev-btn", "n_clicks"),
    Input("next-btn", "n_clicks")
)
def update_graph(graph_type, selected_vars, num_samples, prev_clicks, next_clicks):
    # Ensure at least one variable is selected
    if not selected_vars:
        return px.line(), "Please select at least one variable."

    # Calculate start and end index for slicing
    offset = (next_clicks - prev_clicks) * num_samples
    start_idx = max(0, offset)
    end_idx = min(start_idx + num_samples, len(df))

    # Filter data
    filtered_df = df.iloc[start_idx:end_idx]

    # Create figure based on selected graph type
    if graph_type == 'scatter':
        fig = px.scatter(filtered_df, x=filtered_df.index, y=selected_vars, title="Scatter Plot")
    elif graph_type == 'line':
        fig = px.line(filtered_df, x=filtered_df.index, y=selected_vars, title="Line Chart")
    elif graph_type == 'hist':
        fig = px.histogram(filtered_df, x=selected_vars, title="Distribution Plot")

    # Generate Summary Statistics
    summary_table = filtered_df[selected_vars].describe().to_html()

    return fig, summary_table

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
