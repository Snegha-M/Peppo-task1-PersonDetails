from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models.model import PersonModel

person_args = reqparse.RequestParser()
person_args.add_argument("PersonId", type=int, help="PersonId is required")
person_args.add_argument("PersonName", type=str, help="PersonName is required", required=True)
person_args.add_argument("PersonAge", type=int, help="PersonAge is required", required=True)
person_args.add_argument("PersonAddress", type=str, help="PersonAddress is required", required=True)

person_put_args = reqparse.RequestParser()
person_put_args.add_argument("PersonId", type=int, help="PersonId is required")
person_put_args.add_argument("PersonName", type=str, help="PersonName is required")
person_put_args.add_argument("PersonAge", type=int, help="PersonAge is required")
person_put_args.add_argument("PersonAddress", type=str, help="PersonAddress is required")

resource_fields = {
    "PersonId": fields.Integer,
    "PersonName": fields.String,
    "PersonAge": fields.Integer,
    "PersonAddress": fields.String
}


class Person(Resource):


    @marshal_with(resource_fields)
    @jwt_required()
    def get(self, PersonId):
        result = PersonModel.query.filter_by(PersonId=PersonId).first()
        if not result:
            abort(404, message="Person id is not available")
        return result, 200


    @marshal_with(resource_fields)
    @jwt_required()
    def put(self, PersonId):
        args = person_put_args.parse_args()
        result = PersonModel.query.filter_by(PersonId=PersonId).first()
        #print(result)
        if not result:
            abort(404, message="Person id is not available")

        if args["PersonName"]:
            result.PersonName = args["PersonName"]

        if args["PersonAge"]:
            result.PersonAge = args["PersonAge"]

        if args["PersonAddress"]:
            result.PersonAddress = args["PersonAddress"]

        result.change_in_db()
        return result


    @marshal_with(resource_fields)
    @jwt_required()
    def delete(self, PersonId):
        result = PersonModel.query.filter_by(PersonId=PersonId).first()
        if not result:
            abort(404, message="Person id is not available")
        result.delete_from_db()
        mess = {"Message":"PersonId Deleted"}
        #abort(201, message="personid is deleted")
        return mess,200


class MultiplePerson(Resource):
    @marshal_with(resource_fields)
    @jwt_required()
    def post(self):
        content = request.get_json()
        lst = []
        print(content)
        for x in content:
            person_details = PersonModel(PersonName=x["PersonName"], PersonAge=x["PersonAge"],
                                         PersonAddress=x["PersonAddress"])

            person_details.save_to_db()
            lst.append(person_details)
        return lst, 201