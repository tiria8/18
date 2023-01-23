from dao.director import DirectorDao

class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, did):
        return self.dao.get_one(did)

    def create(self, data):
        return self.dao.create_director(data)

    def update(self, data):
        return self.dao.update_director(data)

    def delete(self, did):
        return self.dao.delete(did)