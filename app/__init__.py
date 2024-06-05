from flask import Flask
from app.main.service.db import init_db
from app.main.router.price import price_bp
from app.main.utils import NotFoundException
from app.main.middleware import handle_not_found_error

def create_app():
    app = Flask(__name__)
    app.register_blueprint(price_bp)
    app.register_error_handler(NotFoundException, handle_not_found_error)
    init_db()
    return app
