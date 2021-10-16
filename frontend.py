from flask import Flask, render_template, send_file
from backend import get_fail
from save_csv import save_to_csv


app = Flask("Price_Server")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    fails = get_fail()
    db["fails"] = fails
    return render_template("report.html", fails=fails)

@app.route("/export")
def export():
    save_to_csv(db["fails"])
    return send_file("fails.csv")

app.run(host="0.0.0.0")
