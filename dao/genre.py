from dao.model.genre import Genre

class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).get.all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def create_genre(self, data):
        new_genre = Genre(**data)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    def update_genre(self, data):
        genre = self.get_one(data.get("id"))
        genre.name = data.get("name")
        self.session.add(genre)
        self.session.commit()

    def delete(self, did):
        genre = self.get_one(did)
        self.session.delete(genre)
        self.session.commit()