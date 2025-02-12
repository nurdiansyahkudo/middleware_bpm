from werkzeug.exceptions import RequestEntityTooLarge
from odoo import http

class LimitedFileSizeMiddleware(http.WebRequest):
    def __call__(self, environ, start_response):
        content_length = environ.get("CONTENT_LENGTH")
        max_size = 2147483648  # 2GB

        if content_length:
            try:
                content_length = int(content_length)
                if content_length > max_size:
                    raise RequestEntityTooLarge(f"File terlalu besar! Maksimum: {max_size} bytes")
            except ValueError:
                pass

        return super().__call__(environ, start_response)
