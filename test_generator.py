import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import numpy as np
from scipy import stats
import plotly.express as px
import dash_html_components as html_comp

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html_comp.Img(src='https://wallpapercave.com/w/WpwaASb.jpg', style={'width': '100%'}),
    html.H1('Statistics Test Generator'),

    html.Label('Data Distribution Type'),
    dcc.Dropdown(
        id='distribution-dropdown',
        options=[
            {'label': 'Normal Distribution', 'value': 'normal'},
            {'label': 'Exponential Distribution', 'value': 'exponential'},
            {'label': 'Uniform Distribution', 'value': 'uniform'}
        ],
        value='normal'
    ),

    html.Label('Sample Size'),
    dcc.Input(id='sample-size-input', type='number', value=100),

    html.Div(id='population-mean-div', children=[
        html.Label('Population Mean', style={'display': 'inline-block'}),
        dcc.Input(id='population-mean-input', type='number', value=0)
    ]),

    html.Div(id='test-output'),
    dcc.Graph(id='distribution-plot')
])

def generate_test_result(data, distribution_type, population_mean):
    if distribution_type == 'normal':
        t_statistic, p_value = stats.ttest_1samp(data, population_mean)
        return f'T-Statistic: {t_statistic}, P-Value: {p_value}'
    elif distribution_type == 'exponential':
        observed, _ = np.histogram(data, bins=10)
        expected = np.array([len(data) / 10] * 10)
        chi2_statistic, p_value = stats.chisquare(observed, expected)
        return f'Chi-square Statistic: {chi2_statistic}, P-Value: {p_value}'
    elif distribution_type == 'uniform':
        ks_statistic, p_value = stats.kstest(data, 'uniform')
        return f'KS Statistic: {ks_statistic}, P-Value: {p_value}'

@app.callback(
    [Output('population-mean-div', 'style')],
    [Input('distribution-dropdown', 'value')]
)
def update_population_mean_visibility(selected_distribution):
    if selected_distribution == 'normal':
        return [{'display': 'inline-block'}]
    else:
        return [{'display': 'none'}]

@app.callback(
    [Output('test-output', 'children'),
     Output('distribution-plot', 'figure')],
    [Input('distribution-dropdown', 'value'),
     Input('sample-size-input', 'value'),
     Input('population-mean-input', 'value')]
)
def update_page_content(distribution_type, sample_size, population_mean):
    if distribution_type == 'normal':
        if population_mean is None or sample_size is None:                          #validation
            data = []
            test_result = "Please provide valid sample size and population mean."
        else:
            data = np.random.normal(population_mean, 1, sample_size)
            test_result = generate_test_result(data, distribution_type, population_mean)
    elif distribution_type == 'exponential':
       if sample_size is None:
            data = []
            test_result = "Please provide valid sample size."
       else:
            data = np.random.exponential(1, sample_size)
            test_result = generate_test_result(data, distribution_type, population_mean)
    elif distribution_type == 'uniform':
       if sample_size is None:
            data = []
            test_result = "Please provide valid sample size."
       else:
        data = np.random.uniform(0, 1, sample_size)
        test_result = generate_test_result(data, distribution_type, population_mean)
    else:
        data = []
        test_result = ""

    fig = px.histogram(data, nbins=20, title='Generated Data Distribution')

    return test_result, fig

if __name__ == '__main__':
    app.run_server(debug=True)