from flask import Flask, jsonify, request
import flask
from data import planet_list

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
  resp = flask.make_response(jsonify({
      "message": "Exoplanet API",
      "planets": planet_list
  }))
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp


@app.route("/planet")
def planet():
  name = request.args.get("name")
  pd = next(item for item in planet_list if item['name'] == name)
  data =  jsonify({
      "message": "Success",
      "data": pd
  }), 200
  resp = flask.make_response(data)
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp


app.run(debug=True)
