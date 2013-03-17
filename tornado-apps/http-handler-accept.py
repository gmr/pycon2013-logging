#!/usr/bin/env python
import logging
from tornado import ioloop, web


class WebRequestHandler(web.RequestHandler):
    """Accepts HTTPHandler POSTs

    """
    def get(self):
        """Return a JSON document of the log entries and flush the
        BufferedLogHandler if there is a flush argument in the URL.

        """
        values = {k: ''.join(v) for k, v in self.request.arguments.iteritems()}
        logging.info('HTTPHandler data: %r', values)
        self.set_status(204)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    routes = [(r'.*', WebRequestHandler)]
    application = web.Application(routes)
    application.listen(8888)
    ioloop.IOLoop.instance().start()
