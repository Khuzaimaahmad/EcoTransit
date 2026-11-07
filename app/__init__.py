from flask import Flask
from flask_migrate import Migrate
from config import Config
from app.database.db import db

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Initialize migrations
    migrate.init_app(app, db)

    # Import models
    from app.models import (
    User, Bus, BusStop, Route, Schedule,
    Connection, Journey, Feedback, PassengerDemand
)

    # Register routes
    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app
