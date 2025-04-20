from flask import Flask
from flask_cors import CORS  
from app.config import bcrypt
from app.auth.routes import auth_bp
from app.tasks.routes import tasks_bp

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}, origins=["https://simple-kanban-board-app.netlify.app"])

    # Initialize extensions
    bcrypt.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    return app
