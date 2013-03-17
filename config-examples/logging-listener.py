#!/usr/bin/env python
import logging
import logging.config
import time

logging.basicConfig(level=logging.INFO)

# Listen on default port of 9030, is a thread
listener = logging.config.listen()
listener.start()

logger = logging.getLogger('listener')

start_time = time.time()
while True:
    logger.info('Time since start: %.2f', time.time() - start_time)
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        logging.config.stopListening()
        break
