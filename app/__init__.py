from flask import Flask
from app.config import config_options

# Initializing application
app = Flask(__name__)

from app import views



