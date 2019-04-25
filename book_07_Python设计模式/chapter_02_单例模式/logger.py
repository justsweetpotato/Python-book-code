#!/usr/bin/env python
# -*- coding: utf-8 -*-

def write_log(level, msg):
    # with open("var/log/filename.log", "a") as log_file:
    with open("filename.log", "a") as log_file:
        log_file.write("[{0}] {1}\n".format(level, msg))


def critical(msg):
    write_log("CRITICAL", msg)


def error(msg):
    write_log("ERROR", msg)
