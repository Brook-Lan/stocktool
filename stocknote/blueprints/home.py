# -*- coding: utf-8 -*-
from flask import render_template, current_app, Blueprint, jsonify


home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    return render_template("home/index.html")