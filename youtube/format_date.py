#!/usr/bin/env python3
# -*- coding: utf8 -*-

import datetime


def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')