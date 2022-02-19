import json
import paho.mqtt.client as mqtt
from flask_cors import CORS, cross_origin
from flask import Flask, request

BROKER_ADDRESS = "192.168.0.82"
client = mqtt.Client("Flask-Server")
client.connect(BROKER_ADDRESS)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})
        
@app.route('/mqtt/rgb', methods=['POST'])
@cross_origin()
def process_json():
    """Ich hasse python"""
    data = json.loads(request.data)
    print(data)
    print(json.dumps(data))
    client.publish("arduino/rgb", json.dumps(data))
    return data
