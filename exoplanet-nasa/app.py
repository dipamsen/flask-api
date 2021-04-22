from flask import Flask, jsonify, request
from data import planet_list

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
  return jsonify({
      "message": "Exoplanet API",
      "planets": planet_list
  }), 200


@app.route("/planet")
def planet():
  name = request.args.get("name")
  pd = next(item for item in planet_list if item['name'] == name)
  return jsonify({
      "message": "Success",
      "data": pd
  }), 200


app.run(debug=True)
