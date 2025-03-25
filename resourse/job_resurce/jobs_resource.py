from flask import jsonify
from flask_restful import Resource, reqparse

from data import db_session
from data.users import User, Jobs
from help_function.function import abort_if_object_not_found
from resourse.job_resurce.parsers import post_parser, put_parser


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_object_not_found(job_id, Jobs)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict()})

    # def post(self):
    #     args = post_parser.parse_args()
    #     session = db_session.create_session()
    #     job = Jobs()
    #     job.team_leader = args['team_leader']
    #     job.job = args['job']
    #     job.work_size = args['work_size']
    #     job.collaborators = args['collaborators']
    #     job.is_finished = args['is_finished']
    #
    #     session.add(job)
    #     session.commit()
    #     return jsonify({'success': 'OK', 'id': job.id})

    def delete(self, job_id):
        abort_if_object_not_found(job_id, Jobs)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, job_id):
        args = put_parser.parse_args()

        abort_if_object_not_found(job_id, Jobs)

        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        if 'team_leader' in args:
            job.name = args['team_leader']
        if 'job' in args:
            job.about = args['job']
        if 'work_size' in args:
            job.email = args['work_size']
        if 'collaborators' in args:
            job.collaborators = args['collaborators']
        if 'is_finished' in args:
            job.is_finished = args['is_finished']

        session.commit()
        return jsonify({'success': 'OK'})

class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        return jsonify({'jobs': [job.to_dict() for job in session.query(Jobs).all()]})

    def post(self):
        args = post_parser.parse_args()
        session = db_session.create_session()
        job = Jobs()
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.is_finished = True if args['is_finished'] == 'True' else False

        session.add(job)
        session.commit()
        return jsonify({'success': 'OK', 'id': job.id})