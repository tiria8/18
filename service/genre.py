from dao.genre import GenreDao


class GenreService:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gig):
        return self.dao.get_one(gig)

    def create(self, data):
        return self.dao.create_genre(data)

    def update(self, data):
        return self.dao.update_genre(data)

    def delete(self, gig):
        return self.dao.delete(gig)