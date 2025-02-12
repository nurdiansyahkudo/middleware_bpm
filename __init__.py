from .middleware.file_size_middleware import LimitedFileSizeMiddleware
from odoo.service.wsgi_server import application

# Tambahkan middleware ke Odoo WSGI application
application = LimitedFileSizeMiddleware(application)
