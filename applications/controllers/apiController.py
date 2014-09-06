#!/usr/bin/env python
# encoding=utf-8

from flask import Blueprint
from applications.Service import redisService
import json

mod = Blueprint("api", __name__)


@mod.route('/api/set/<key>/<val>')
def set_id(key, val):
    return json.dumps(redisService.setValueList(key, val), indent=2)

