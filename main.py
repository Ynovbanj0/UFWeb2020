from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

from passlib.hash import sha256_crypt  # Use for password hashing

from models import db
from application import app
from models import *

import urllib3
import json
import pymysql

import config

http = urllib3.PoolManager()
db.init_app(app)

@app.route("/", methods=["POST", "GET"])
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
