from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from src.config import Config
from src.setup_db import db
from src.views.directors import director_ns
from src.views.genres import genre_ns
from src.views.movies import movie_ns
from src.views.users import user_ns
from src.views.auth import auth_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    Migrate(application, db)
    api = Api(application)
    # регистрация пространств имён
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
