from flask import Flask
from flask_cors import CORS
import connexion

app = connexion.FlaskApp(__name__)

from app import usersData
