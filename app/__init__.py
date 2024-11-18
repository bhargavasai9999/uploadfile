from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///secure_file_sharing.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from .routes import auth, file, client
    app.register_blueprint(auth.bp, url_prefix='/auth')
    app.register_blueprint(file.bp, url_prefix='/file')
    app.register_blueprint(client.bp, url_prefix='/client')

    return app
