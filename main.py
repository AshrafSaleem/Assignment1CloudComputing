#!/usr/bin/env python
# encoding: utf-8
import json
from object_detection import object_detection
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/api/object_detection', methods=["POST"])
def object_detection_server():
    client_data = json.loads(json.loads(request.data))
    result = object_detection(client_data["image"])
    return jsonify({"id": client_data["id"], "objects": result})

app.run(debug = True, threaded = True)