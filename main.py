#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/api/object_detection', methods=["POST"])
def object_detection():
    client_data = json.loads(request.data)
    return jsonify(client_data)

app.run(debug = True)