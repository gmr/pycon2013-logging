#!/usr/bin/env python

import logging.config
import socket
import struct

HOST = 'localhost'
PORT = logging.config.DEFAULT_LOGGING_CONFIG_PORT  # 9030


def send_conf(config_text):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(struct.pack('>L', len(config_text)))
    s.send(config_text)
    s.close()

with open('logging.cfg', 'r') as handle:
    send_conf(handle.read())
