import psycopg2

from src.config import Config
from src.app import create_app
from src.setup_db import db

if __name__ == '__main__':
    with create_app(Config()).app_context():
        db.drop_all()
        db.create_all()
