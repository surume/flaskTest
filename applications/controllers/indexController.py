#!/usr/bin/env python
# encoding=utf-8

from flask import Blueprint

mod = Blueprint("index", __name__)

@mod.route('/')
def hello_world():
    return "FlaskTest!"
