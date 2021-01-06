#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import Connect


class Resource:
    def __init__(self, row: tuple):
        self.video_path = row[0]
        self.pic_path = row[1]


