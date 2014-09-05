#!/usr/bin/env python
# encoding=utf-8

import os
from flask import Flask
import logging
import redis

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

