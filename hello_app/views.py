from datetime import datetime
from flask import Flask, render_template, request
from . import app
import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

BBSERVICE = BlockBlobService("wkiotstorage", "qMcTb8K1JhczbBmPrhboc3RZk1hYszYe0RKVe8Ba0lxEKqhDhuZZYVRuUnDWk/90XaCew4bJqN/AGcseWLf9Dw==")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/upload/')
def upload():
   return render_template("upload.html")

@app.route("/uploader/", methods = ['GET', 'POST'])
def uploader():
    f = request.files['inputFile']

    BBSERVICE.create_blob_from_stream("music",f.filename ,f)

    return render_template(
        "uploaded.html",
        fname = f.filename)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
