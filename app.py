from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Buy Groceries",
        "description": "Milk, Cheese, Pizza, Fruits",
        "done": False
    },
    {
        "id": 2,
        "title": "Learn Python",
        "description": "Learn Python Web Development",
        "done": False
    }
]


@app.route("/")
def hello_world():
  return "hello, world!"


@app.route("/add-data", methods=["POST"])
def add_data():
  if not request.json:
    return jsonify({"status": "error", "message": "Please provide the Data."}, 400)
  task = {
      "id": tasks[-1]["id"] + 1,
      "title": request.json["title"],
      "description": request.json.get("description", ""),
      "done": False
  }
  tasks.append(task)
  return jsonify({"status": "Success", "message": "Task added successfully."})


@app.route("/get-data")
def get_data():
  return jsonify({"data": tasks})


if __name__ == "__main__":
  app.run(debug=True)
