from flask import Flask
from app.config import config_options

# Initializing application
app = Flask(__name__, instance_relative_config = True)

from app import views



