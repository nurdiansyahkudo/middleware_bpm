from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import RequestEntityTooLarge

class LimitedFileSizeMiddleware:
    def __init__(self, app, max_size=2 * 1024 * 1024 * 1024):  # 2GB
        self.app = app
        self.max_size = max_size

    def __call__(self, environ, start_response):
        content_length = environ.get("CONTENT_LENGTH")
        
        if content_length:
            try:
                content_length = int(content_length)
                if content_length > self.max_size:
                    raise RequestEntityTooLarge(f"File terlalu besar! Maksimum: {self.max_size} bytes")
            except ValueError:
                pass
        
        return self.app(environ, start_response)
