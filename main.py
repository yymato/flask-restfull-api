import base64
from io import BytesIO

import requests
from flask import Flask, make_response, jsonify, render_template
from flask_login import LoginManager
from flask_restful import Api


from data import db_session
from data.db_session import create_session
from data.users import User
from resourse.job_resurce.jobs_resource import JobsListResource, JobsResource
from resourse.user_resource.users_resource import UsersListResource, UsersResource

app = Flask(__name__)
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# для списка объектов
api.add_resource(UsersListResource, '/api/v2/users')
api.add_resource(JobsListResource, '/api/v2/jobs')

# для одного объекта
api.add_resource(UsersResource, '/api/v2/users/<int:user_id>')
api.add_resource(JobsResource, '/api/v2/jobs/<int:job_id>')


def main():
    db_session.global_init('data/123.sqlite')
    app.run()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)

if __name__ == '__main__':
    main()