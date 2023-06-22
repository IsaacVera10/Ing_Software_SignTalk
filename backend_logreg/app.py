from flask import Flask
from flask_dynamo import Dynamo
from flask_cors import CORS
import key_config as keys
import boto3
import os

# Genera una clave secreta aleatoria
def generate_secret_key():
    return os.urandom(16).hex()


app = Flask(__name__)
app.secret_key = generate_secret_key()

# Configuración de CORS
cors = CORS(app, resources={r"/*": {"origins": "*"}})

dynamodb = boto3.resource(
    'dynamodb', region_name='us-east-1',
    aws_access_key_id=keys.ACCESS_KEY_ID,
    aws_secret_access_key=keys.ACCESS_SECRET_KEY,
    aws_session_token=keys.AWS_SESSION_TOKEN)

import views