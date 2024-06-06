from flask import Flask

from app.main.database import create_session, init_db
from app.main.middleware.handler import handle_not_found_error
from app.main.router.price_router import price_bp
from app.main.utils import NotFoundException


def create_app():
    app = Flask(__name__)
    app.register_blueprint(price_bp)
    app.register_error_handler(NotFoundException, handle_not_found_error)

    init_db()
    with app.app_context():
        app.db_session = create_session()

    return app
