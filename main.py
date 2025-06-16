# main.py
from flask import Flask, render_template_string
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string(open("index.html").read())

if __name__ == "__main__":
    app.run(debug=True)
