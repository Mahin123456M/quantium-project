import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

data = pd.read_csv('../combinedSales.csv')

data['sales'] = data['sales'].str.replace('$', '').astype(float)

data['date'] = pd.to_datetime(data['date'])

# Group by date and sum sales across all regions
totalSales = data.groupby('date')['sales'].sum().reset_index()
totalSales = totalSales.sort_values('date')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis", style={'textAlign': 'center', 'marginBottom': 30}),
    
    html.Div([
        dcc.Graph(
            id='sales-chart',
            figure=px.line(
                totalSales,
                x='date',
                y='sales',
                title='Pink Morsel Sales Over Time',
                labels={'date': 'Date', 'sales': 'Total Sales ($)'},
                markers=True,
                height=600
            )
        )
    ]),
    

])

if __name__ == '__main__':
    app.run(debug=True)
