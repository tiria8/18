from flask import request
from flask_restx import Namespace, Resource

from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')

@directors_ns.route('/')
class DirectorsView(Resource):
    def get_all(self):
        all_directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(all_directors)
        return result, 200

    def post(self):
        request_json = request.json
        new_director = director_service.create(request_json)
        return "", 201, {"location": f"\\directors\\{new_director.id}"}

@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return DirectorSchema().dump(director), 200

    def put(self, did):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = did
        director_service.update(request_json)
        return "", 204

    def delete(self, did):
        director_service.delete(did)
        return "", 204
