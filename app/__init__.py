from flask import Flask
from app.database import init_db
from app.routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)

    app.register_blueprint(main_bp)

    return app
