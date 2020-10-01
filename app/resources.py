from flask_restful import Resource, request
from .models import UserModel
from .schemas import UserSchema
from flask_jwt import jwt_required


class UserResource(Resource):
    def post(self):
        candidate = request.get_json()
        schema = UserSchema()
        errors = schema.validate(candidate)
        if errors:
            return {'message': errors}, 400
        data = schema.dump(candidate)
        if UserModel.get_by_email(data['email']):
            return {'message': 'user with this email already register'}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'message ': 'user was created'}, 201

    @jwt_required()
    def get(self):
        users = UserModel.query.all()
        schema = UserSchema()
        return schema.dump(users, many=True), 200
