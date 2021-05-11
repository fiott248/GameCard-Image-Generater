import flask
from flask import request, jsonify
from functions import GeneID, upload_file, createArt

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/test', methods=['GET'])
def test():
    return jsonify(createArt(GeneID()))

@app.route('/Upload', methods=['POST'])
def Upload():
    return jsonify(UploadAssest())
app.run()