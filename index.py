#!/usr/bin/env python
# encoding=utf-8

import os
from flask import Flask
import logging
import redis
import json

conn = redis.StrictRedis(host='localhost', port=6379)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    # filename='/tmp/myapp.log',
                    # filemode='w'
                    )


logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bows')


app = Flask(__name__)
app.config.update({'DEBUG': True })


@app.route('/')
def hello_world():
        return "Hello World!"


@app.route('/api/set/<key>/<val>')
def set_id(key, val):
    redisKey = 'redis_' + key
    twit_id = str(val)
    logging.debug("redis_keys:"+twit_id)
    conn.rpush(redisKey, twit_id)
    resultlist = conn.lrange(redisKey, 0, -1)
    decodeList = [x.decode() for x in resultlist ]
    return json.dumps(decodeList, indent=2)




















if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

