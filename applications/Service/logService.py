#!/usr/bin/env python
# encoding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    # filename='/tmp/myapp.log',
                    # filemode='w'
)


def debug_log(msg):
    logging.debug(msg)


def info_log(msg):
    logging.info(msg)


def warning_log(msg):
    logging.warning(msg)
