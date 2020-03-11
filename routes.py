from flask import render_template
import sys
import os
from Untitled12 import app
@render_template.route("/")
@render_template.route("/index")
@render_template.route("/home")
def index():
    return "index.html", login