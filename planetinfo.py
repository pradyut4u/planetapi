from flask import Flask
from flask import jsonify
from flask import request
from planetdata import data

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "data":data,
        "message":"message"
    }),200

@app.route("/search")
def search():
    name = request.args.get("name")
    planetdata = next(item for item in data if item["name"] == name)
    return jsonify({
        "planetdata":planetdata,
        "message":"message"
    }),200

if __name__ == "__main__":
    app.run()