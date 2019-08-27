# Entry point for the application.
import flask
app = flask.Flask(__name__)
from . import views  # For import side-effects of setting up routes
