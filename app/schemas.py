from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=[Length(6, 20, error='password must be 6-20 characters')])
    name = fields.String(validate=Length(2, 20, error='name must be 6-20 characters'), required=True)
