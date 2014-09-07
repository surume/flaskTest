#!/usr/bin/env python
# encoding=utf-8

import os
import redis
from applications.Service import logService

REDIS_TO_GO_URL = 'REDISTOGO_URL'
REDIS_LOCAL_URL = 'redis://localhost:6379'

redis_url = os.getenv(REDIS_TO_GO_URL, REDIS_LOCAL_URL)
redis = redis.from_url(redis_url)


def set_value_list(key, val):
    if key is None:
        return None
    if val is None:
        return None

    now_result = get_value_list(key)
    is_val_exist = [result for result in now_result if result == val]
    if is_val_exist:
        return now_result

    redis.rpush(key, str(val))
    return get_value_list(key)


def get_value_list(key):
    result_list = redis.lrange(key, 0, -1)
    if result_list is None:
        return None
    return [x.decode() for x in result_list]
