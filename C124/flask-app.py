from flask import Flask, jsonify, request

app = Flask(__name__)


contacts = [{"name": "Dipam Sen", "contact": "8274725028", "id": 1}]


@app.route("/")
def index():
    return jsonify({"message": "Hello, World!"}), 200


@app.route("/get-contacts")
def get_data():
    return jsonify({"contacts": contacts}), 200


@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({"status": "error", "message": "No Data provided"})
    contact = {
        "name": request.json["name"],
        "contact": request.json.get("contact", ""),
        id: contacts[-1]["id"] + 1,
    }
    contacts.append(contact)
    return jsonify({"status": "ok", "message": "Successfully added contact"})


if __name__ == "__main__":
    app.run(debug=True)