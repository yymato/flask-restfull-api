from flask import jsonify
from flask_restful import Resource, reqparse

from data import db_session
from data.users import User
from help_function.function import abort_if_object_not_found
from resourse.user_resource.parsers import post_parser, put_parser


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_object_not_found(user_id, User)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict()})

    def post(self):
        args = post_parser.parse_args()
        session = db_session.create_session()
        user = User()
        user.name = args['name']
        user.about = args['about']
        user.email = args['email']
        user.set_password(args['password'])

        session.add(user)
        session.commit()
        return jsonify({'success': 'OK', 'id': user.id})

    def delete(self, user_id):
        abort_if_object_not_found(user_id, User)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        args = put_parser.parse_args()

        abort_if_object_not_found(user_id, User)

        session = db_session.create_session()
        user = session.query(User).get(user_id)
        if args['name']:
            user.name = args['name']
        if args['about']:
            user.about = args['about']
        if args['email']:
            user.email = args['email']
        if args['password']:
            user.set_password(args['password'])

        session.commit()
        return jsonify({'success': 'OK'})

class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        return jsonify({'users': [user.to_dict() for user in session.query(User).all()]})

    def post(self):
        args = post_parser.parse_args()
        session = db_session.create_session()
        user = User()
        user.name = args['name']
        user.about = args['about']
        user.email = args['email']
        user.set_password(args['password'])

        session.add(user)
        session.commit()
        return jsonify({'success': 'OK', 'id': user.id})