import plotly.express as px
import dash_bootstrap_components as dbc
import dash
from dash import dash_table
import dash_cytoscape as cyto
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State, ALL, MATCH
import dash_daq as daq
import flask

from pre_serve import *
import sub_app1
import sub_app2

topbar = dbc.NavbarSimple(
    children=[
          dbc.Button(html.Img(src='./ham.png',
                               style={'height':'25px'}), outline=True, color="secondary", className="mr-1",
                               id="btn_sidebar"),
    ],
    brand="Demo",
    brand_href="/",
    color="dark",
    dark=True,
    fluid=True,
)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 56,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.35s",
    "padding": "0.5rem 1rem",
    "background-color": "#eeeeee",
}

SIDEBAR_HIDDEN = {
    "position": "fixed",
    "top": 56,
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.35s",
    "padding": "0rem 0rem",
    "background-color": "#eeeeee",
}


CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "Transparent",
}

CONTENT_STYLE_HIDDEN = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "Transparent",
}


sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("app1", href="/app1/", id="a1-link"),
                dbc.NavLink("app2", href="/app2/", id="a2-link"),
                dbc.NavLink("home page", href="/", id="EMPTY-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_HIDDEN,
)



Layout1 = [html.H1('Home Page')]
app.layout = html.Div([html.Div(children = [
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='side_click'),
    topbar,
    sidebar] , id='navbar_and_sidebar'),
    html.Div(Layout1, id='page-content')])



@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return Layout1
    elif pathname == '/app1/' or pathname == '/app1':
        return sub_app1.layout
    elif pathname == '/app2/' or pathname == '/app2':
        return sub_app2.layout
    else:
        return html.H1("404 this is not the page you're looking for")
        
        
        
@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],
    [Input("btn_sidebar", "n_clicks"),],
    [State("side_click", "data"),]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDDEN
            content_style = CONTENT_STYLE_HIDDEN
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_HIDDEN
        content_style = CONTENT_STYLE_HIDDEN
        cur_nclick = 'HIDDEN'
    return sidebar_style, content_style, cur_nclick

        
if __name__ == '__main__':
    app.run_server(debug=True)

