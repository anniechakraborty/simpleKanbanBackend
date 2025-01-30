from flask import Flask
from app.auth import auth_bp
from app.tasks import tasks_bp
from app.extensions import db

def create_app():
    app = Flask(__name__)
    
    # Load Config
    app.config.from_object('app.config.Config')

    # Initialize Database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    return app
