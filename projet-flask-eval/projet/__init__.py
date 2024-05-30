from flask import Flask

app = Flask("projet",static_folder='static')

from projet.models import *
from projet.config import *
from projet import configdatabase
from projet.controllers import *
