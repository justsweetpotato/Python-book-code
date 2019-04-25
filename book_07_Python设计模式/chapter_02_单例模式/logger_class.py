#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def _write_log(self, level, msg):
        with open(self.file_name, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def error(self, msg):
        self._write_log("ERROR", msg)
