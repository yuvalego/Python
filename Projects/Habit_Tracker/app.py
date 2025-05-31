import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import html, dcc

# Step 1: Read Data
def read_data(files):
    dataframes = {}
    for file in files:
        df = pd.read_csv(f'{file}.csv', parse_dates=['Date'])
        dataframes[file] = df
    return dataframes

# Step 2: Data Processing
def process_data(dataframes):
    processed_data = {}
    for file, df in dataframes.items():
        processed_data[file] = df
    return processed_data

files = ['sleep', 'water_intake', 'protein_intake', 'training_time', 'training_types']
dataframes = read_data(files)
processed_data = process_data(dataframes)

# Sleep Data
sleep_data = processed_data['sleep']
sleep_fig = px.line(sleep_data, x='Date', y='Sleep Duration', title='Sleep Duration')

# Water Intake Data
water_data = processed_data['water_intake']
water_fig = px.bar(water_data, x='Date', y='Total Water Intake (liters)', title='Water Intake')

# Protein Intake Data
protein_data = processed_data['protein_intake']
protein_fig = px.bar(protein_data, x='Date', y='Total Protein Intake (grams)', title='Protein Intake')

# Training Duration Data
training_data = processed_data['training_time']
training_fig = px.line(training_data, x='Date', y='Training Duration (hours)', title='Training Duration')

# Training Types Data
training_types_data = processed_data['training_types']
training_types_fig = px.pie(training_types_data, names='Training Type', title='Training Types')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Life Tracker'),
    dcc.Graph(figure=sleep_fig),
    dcc.Graph(figure=water_fig),
    dcc.Graph(figure=protein_fig),
    dcc.Graph(figure=training_fig),
    dcc.Graph(figure=training_types_fig),
])

if __name__ == '__main__':
    app.run_server(debug=True)
