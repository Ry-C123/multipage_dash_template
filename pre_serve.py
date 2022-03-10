import dash
import flask
import dash_bootstrap_components as dbc

#### Start Dash app #####
SERV = flask.Flask(__name__)
app = dash.Dash(__name__, url_base_pathname='/', server=SERV, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Demo'

