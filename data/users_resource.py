from flask import jsonify
from users import User
from flask_restful import Resource, reqparse
from news_api import abort_if_news_not_found
import db_session

parser = reqparse.RequestParser()
parser.add_argument('id', required=True, type=int)
parser.add_argument('name', required=True, type=str)
parser.add_argument('about', required=True, type=str)
parser.add_argument('hashed_password', required=True)
parser.add_argument('created_date', required=True)


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_news_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify({'news': users.to_dict(
            only=('id', 'name', 'about', 'email'))})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        users = session.query(User).get(news_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'about', 'name')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            id=args['id'],
            name=args['name'],
            about=args['about'],
            email=args['email'],
            hashed_passsword=args['hashed_passsword'],
            created_date=args['created_date']
        )
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})
