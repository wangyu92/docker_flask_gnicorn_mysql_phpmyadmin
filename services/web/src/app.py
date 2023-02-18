from flask import (
    Flask, render_template, request, redirect, session, abort,
    jsonify, send_from_directory)
from sqlalchemy import create_engine


app = Flask(__name__)
app.config.from_object("src.config.Config")
db = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])


@app.route("/")
def index():
    return jsonify({"message": "Hello, World!"})


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)
