from src.dao.director import DirectorDAO
from src.dao.genre import GenreDAO
from src.dao.movie import MovieDAO
from src.dao.user import UserDao
from src.service.director import DirectorService
from src.service.genre import GenreService
from src.service.movie import MovieService
from src.setup_db import db
from src.service.user import UserService

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)

user_dao = UserDao(session=db.session)
user_service = UserService(dao=user_dao)
