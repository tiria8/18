from flask import request
from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')

@genres_ns.route('/')
class GenresView(Resource):
    def get_all(self):
        all_genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(all_genres)
        return result, 200

    def post(self):
        request_json = request.json
        new_genre = genre_service.create(request_json)
        return "", 201, {"location": f"\\genres\\{new_genre.id}"}

@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gig):
        genre = genre_service.get_one(gig)
        return GenreSchema().dump(genre), 200

    def put(self, gig):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = gig
        genre_service.update(request_json)
        return "", 204

    def delete(self, gig):
        genre_service.delete(gig)
        return "", 204
