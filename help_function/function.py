from flask_restful import abort

from data import db_session


def abort_if_object_not_found(object_id: int, instance: object):
    session = db_session.create_session()
    news = session.query(instance).get(object_id)
    if not news:
        abort(404, message=f"User {object_id} not found")
