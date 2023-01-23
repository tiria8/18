from dao.movie import MovieDao

class MovieService:
    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_all(self, data):
        if data.get('director_id') is not None:
            movies = self.dao.get_by_director_id('director_id')
        if data.get('genre_id') is not None:
            movies = self.dao.get_by_director_id('genre_id')
        if data.get('year') is not None:
            movies = self.dao.get_by_director_id('year')
        else:
            movies = self.dao.get_all()
        return movies

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create_movie(data)

    def update(self, data):
        return self.dao.update_movie(data)

    def delete(self, mid):
        return self.dao.delete(mid)