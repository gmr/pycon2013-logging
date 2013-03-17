#!/usr/bin/env python
import logging
from logging import handlers
import socket
import traceback

HOST = 'localhost'
FROM = '"APPLICATION ALERT" <python@your-domain>'
TO = 'you@your-domain'
SUBJECT = 'New Critical Event From [APPLICATION]'

# Setup logging
logging.basicConfig(level=logging.INFO)

handler = handlers.SMTPHandler(HOST, FROM, TO, SUBJECT)
email_logger = logging.getLogger('smtp.example')
email_logger.addHandler(handler)
email_logger.setLevel = logging.CRITICAL

logging.info('Root logger output')
try:
    email_logger.critical('Critical Event Notification\n\nTraceback:\n %s',
                          ''.join(traceback.format_stack()))
except socket.error as error:
    logging.critical('Could not send email via SMTPHandler: %r', error)
