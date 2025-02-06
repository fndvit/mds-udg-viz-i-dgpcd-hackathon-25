from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/output.csv")
def serve_csv():
    return send_file("output.csv", mimetype="text/csv")

app.run(port=8000)
