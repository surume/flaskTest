#!/usr/bin/env python
# encoding=utf-8

import os
from flask import Flask
from applications.controllers import indexController, apiController

app = Flask(__name__)

mods = [indexController.mod, apiController.mod]
[app.register_blueprint(mod) for mod in mods]

app.config.update({'DEBUG': True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
