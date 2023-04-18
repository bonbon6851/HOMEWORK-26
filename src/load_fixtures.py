from contextlib import suppress

from sqlalchemy.exc import IntegrityError

from src.config import Config
from src.dao.model.genre import Genre
from src.dao.model.movie import Movie
from src.dao.model.director import Director
from src.app import create_app
from src.setup_db import db
from src.utils import read_json


def load_data(data, model) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures = read_json("fixtures.json")

    with create_app(Config()).app_context():
        load_data(fixtures['movies'], Movie)
        load_data(fixtures['genres'], Genre)
        load_data(fixtures['directors'], Director)

        with suppress(IntegrityError):
            db.session.commit()
