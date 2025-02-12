from odoo.http import Request

class LimitedFileSizeMiddleware(Request):
    def __init__(self, application, max_size=2 * 1024 * 1024 * 1024):  # 2GB
        self.application = application
        self.max_size = max_size

    def __call__(self, environ, start_response):
        if 'CONTENT_LENGTH' in environ:
            content_length = int(environ['CONTENT_LENGTH'])
            if content_length > self.max_size:
                start_response('413 Request Entity Too Large', [('Content-Type', 'text/plain')])
                return [b'File too large']
        return self.application(environ, start_response)
