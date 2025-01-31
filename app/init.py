from flask import Flask
from app.extensions import bcrypt
from app.auth.routes import auth_bp
from app.tasks.routes import tasks_bp

def create_app():
    app = Flask(__name__)

    # Initialize extensions
    bcrypt.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    return app
