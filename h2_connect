from flask import request
from flask_restful import Resource, abort
from marshmallow import ValidationError
import persistence

class Exoplanet(Resource):
    def get(self, Id=None):
        if Id is None:
            return persistence.get_all()

        exoplanet = persistence.get(Id)
        if not exoplanet:
            abort(404, errors={"errors": {"message": "Exoplanet with Id {} does not exist".format(Id)}})
        return exoplanet

    def post(self):
        try:
            exoplanet = ExoplanetSchema(exclude=["id"]).loads(request.json)
            if not persistence.create(exoplanet):
                abort(404, errors={"errors": {"message": "Exoplanet with name {} already exists".format(request.json["name"])}})
        except ValidationError as e:
            abort(405, errors=e.messages)

    def put(self, Id):
        try:
            exoplanet = ExoplanetSchema(exclude=["id"]).loads(request.json)
            if not persistence.update(exoplanet, Id):
                abort(404, errors={"errors": {"message": "Exoplanet with Id {} does not exist".format(Id)}})
        except ValidationError as e:
            abort(405, errors=e.messages)

    def delete(self, Id):
        if not persistence.delete(Id):
            abort(404, errors={"errors": {"message": "Exoplanet with Id {} does not exist".format(Id)}})
