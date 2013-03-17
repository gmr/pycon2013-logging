#!/usr/bin/env python
import logging
from logging import handlers
import socket
import traceback

HOST = 'localhost'
PORT = 8888

# Setup logging
logging.basicConfig(level=logging.INFO)

handler = handlers.HTTPHandler('%s:%s' % (HOST, PORT), '/')
http_logger = logging.getLogger('http.example')
http_logger.addHandler(handler)
http_logger.setLevel = logging.CRITICAL

logging.info('Root logger output')
try:
    http_logger.critical('Critical Event Notification\n\nTraceback:\n %s',
                         ''.join(traceback.format_stack()))
except socket.error as error:
    logging.critical('Could not deliver message via HTTPHandler: %r', error)
