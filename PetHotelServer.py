# Where our server requests will be

#flask imports
from flask import Flask, request, jsonify
#import con from connectionFunction.py
from connFunction import con
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'