from dao.director import DirectorDao
from dao.genre import GenreDao
from dao.movie import MovieDao

from service.movie import MovieService
from service.genre import GenreService
from service.director import DirectorService

from setup_db import db

director_dao = DirectorDao(session=db.session)
genre_dao = GenreDao(session=db.session)
movie_dao = MovieDao(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)