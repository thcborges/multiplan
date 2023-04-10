from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.MINTY],
)
print(1)

rent_the_runway = pd.read_parquet('data/rent_the_runway.parquet')
print(2)
weight_histogram = pd.read_parquet('data/weight_histogram.parquet')
print(3)
fit = pd.read_parquet('data/fit.parquet')
print(4)
category_size = pd.read_parquet('data/category_size.parquet')
print(5)
navbar = dbc.NavbarSimple(
    brand='Rent The Runway',
    brand_href='#',
    color='primary',
    dark=True,
)

weight_histogram = dcc.Graph(
    figure=px.histogram(
        weight_histogram,
        x='Peso em Kg',
        title='Distribuição de peso em Kilograma',
    )
)

fit_absolut = dcc.Graph(
    figure=px.bar(
        fit,
        x='Rented for',
        y='Fit',
        title='Quantidade absoluta de Fit',
    )
)

fit_percent = dcc.Graph(
    figure=px.bar(
        fit.sort_values('Porcentagem', ascending=False),
        x='Rented for',
        y='Porcentagem',
        title='Quantidade relativa de Fit',
    )
)

cloud_word = html.Div(
    children=[html.Img(src=app.get_asset_url('wordcloud.png'))]
)

category_size_tab = (
    html.Div(
        children=[
            html.P('Quantidade de peças alugadas por categoria'),
            dbc.Label('Categoria', html_for='select-category-size'),
            dcc.Dropdown(
                options=category_size['category'].unique(),
                value='dress',
                id='select-category-size',
            ),
            dcc.Graph(figure={}, id='histogram-category-size'),
        ]
    ),
)
print(6)
app.layout = html.Div(
    children=[
        navbar,
        dbc.Container(
            [
                dbc.Tabs(
                    [
                        dbc.Tab(weight_histogram, label='Histograma de peso'),
                        dbc.Tab(
                            fit_absolut, label='Quantidade absoluta de fit'
                        ),
                        dbc.Tab(
                            fit_percent, label='Quantidade percentual de fit'
                        ),
                        dbc.Tab(cloud_word, label='Nuvem de Palavras'),
                        dbc.Tab(
                            category_size_tab, label='Tamanho por Categoria'
                        ),
                    ]
                ),
                dash_table.DataTable(
                    data=fit.sort_values('Porcentagem').to_dict('records'),
                    page_size=10,
                ),
                dash_table.DataTable(
                    data=rent_the_runway[
                        [
                            'fit',
                            'bust size',
                            'Peso em Kg',
                            'weight',
                            'rating',
                            'rented for',
                            'body type',
                            'category',
                            'height',
                            'size',
                            'age',
                        ]
                    ].to_dict('records'),
                    page_size=10,
                ),
            ]
        ),
    ]
)


print(7)
# Add controls to build the interaction
@callback(
    Output(
        component_id='histogram-category-size', component_property='figure'
    ),
    Input(component_id='select-category-size', component_property='value'),
)
def update_graph(col_chosen):
    print(8)
    df = category_size.loc[category_size['category'] == col_chosen]
    fig = px.bar(df, x='size', y='count')
    return fig


server = app.server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
