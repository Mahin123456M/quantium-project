import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load and process data
data = pd.read_csv('../combinedSales.csv')
data['sales'] = data['sales'].str.replace('$', '').astype(float)
data['date'] = pd.to_datetime(data['date'])

# Group by date and region, sum sales
regional_sales = data.groupby(['date', 'region'])['sales'].sum().reset_index()
regional_sales = regional_sales.sort_values('date')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis", className='header'),
    
    html.Div([
        html.Label("Select Region:", className='radio-label'),
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'marginRight': '20px', 'fontSize': '16px'},
            className='radio-items'
        )
    ], className='radio-container'),
    
    html.Div([
        dcc.Graph(
            id='sales-chart',
            config={'displayModeBar': False}
        )
    ], className='chart-container'),
    
    html.Div([
        html.P(
            "This interactive chart visualizes Pink Morsel sales over time. Use the radio buttons above to filter by region and answer whether sales were higher before or after the price increase on January 15, 2021.",
            className='description'
        )
    ])
], className='container')

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        # Sum across all regions
        filtered_data = regional_sales.groupby('date')['sales'].sum().reset_index()
        title = 'Total Pink Morsel Sales Over Time (All Regions)'
    else:
        # Filter by selected region
        filtered_data = regional_sales[regional_sales['region'] == selected_region]
        title = f'Pink Morsel Sales Over Time ({selected_region.capitalize()} Region)'
    
    filtered_data = filtered_data.sort_values('date')
    
    figure = px.line(
        filtered_data,
        x='date',
        y='sales',
        title=title,
        labels={'date': 'Date', 'sales': 'Sales ($)'},
        markers=True,
        height=600,
        color_discrete_sequence=['#3498db']
    )
    
    figure.update_layout(
        title_font_size=20,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='#f8f9fa'
    )
    
    return figure

if __name__ == '__main__':
    app.run(debug=True)
