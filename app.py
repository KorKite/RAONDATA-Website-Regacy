from flask import Flask
from flask import render_template, redirect, url_for, flash, request
import json
import slackmachine
# from .db import write
app = Flask(__name__)
app.secret_key = 'fsdakljq@2lk39fwad!asf'

@app.route("/")
def home():

    with open("webdata/projectinfo.json") as f:
        projects = json.load(f)
    return render_template("re_main.html", projects=projects)


@app.route("/ask")
def ask():
    return render_template("re_ask.html")


@app.route("/project")
def project():
    return render_template("re_ask.html")

@app.route("/human")
def human():
    with open("webdata/teaminfo.json") as f:
        humans = json.load(f)
    return render_template("about_us.html",humans=humans)


@app.route("/submit", methods=["get"])
def submit():
    email = request.args.get("Email")
    name = request.args.get("name")
    group = request.args.get("group")
    contents = request.args.get("contents")  
    agree = request.args.get("agree")
    if agree == "on":
        agree = "동의함"
    else:
        agree = "동의하지 않음"
    print(agree)
    data = {
        "email":email,
        "name": name,
        "group":group,
        "contents":contents,
        "agree":agree
    }
    slackmachine.sending(data)  
    return redirect(url_for("home"))

if(__name__ == "__main__"):
    app.run(port=8887, debug=True, host='0.0.0.0',)