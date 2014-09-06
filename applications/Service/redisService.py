#!/usr/bin/env python
# encoding=utf-8

import os
import redis

REDIS_TO_GO_URL = 'REDISTOGO_URL'
REDIS_LOCAL_URL = 'redis://localhost:6379'

redis_url = os.getenv(REDIS_TO_GO_URL, REDIS_LOCAL_URL)
redis = redis.from_url(redis_url)


def setValueList(key, val):
    if key is None:
        return None
    if val is None:
        return None

    redis.rpush(key, str(val))
    result_list = redis.lrange(key, 0, -1)
    return [x.decode() for x in result_list]


