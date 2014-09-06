#!/usr/bin/env python
# encoding=utf-8

# import flask
import unittest
from builtins import print

import index
import logging
from applications.Service import redisService


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.app = index.app.test_client()

    def test_get(self):
        response = self.app.get('/')
        assert response.status_code == 200
        logging.debug(response.data)
        assert response.data == b'FlaskTest!'




class TestApiController(unittest.TestCase):

    def setUp(self):
        redisService.redis.flushall()

    def test_null_keys(self):
        key = None
        val = "val"
        assert None == redisService.setValueList(key, val)

    def test_null_val(self):
        key = "key"
        val = None
        assert None == redisService.setValueList(key, val)

    def test_all_null(self):
        key = None
        val = None
        assert None == redisService.setValueList(key, val)

    def test_nomal(self):
        redisService.redis.flushall()
        key = "key"
        val = "val"
        assert ['val'] == redisService.setValueList(key, val)

if __name__ == '__main__':
    unittest.main()
