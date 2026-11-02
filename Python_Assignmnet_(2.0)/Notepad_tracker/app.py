
from flask import Flask, render_template, request, jsonify
import os
import subprocess

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/open", methods=["POST"])


if __name__ == "__main__":
    app.run(debug=True)
