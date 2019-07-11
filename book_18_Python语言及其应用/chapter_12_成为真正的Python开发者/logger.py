#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(
    level='DEBUG',
    # filename='warn.log',
    format='%(levelname)s:%(asctime)s:%(name)s %(module)s:%(message)s'
)
logger = logging.getLogger('Zhang')
try:
    num = 1 / 0
except Exception as e:
    logger.error(e, exc_info=True)
    # 等同于
    # logging.exception(e)

