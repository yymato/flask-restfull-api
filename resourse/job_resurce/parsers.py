from flask_restful import reqparse

post_parser = reqparse.RequestParser()
post_parser.add_argument('team_leader', required=True)
post_parser.add_argument('job', required=True)
post_parser.add_argument('work_size', required=True)
post_parser.add_argument('collaborators', required=True)
post_parser.add_argument('is_finished', required=True)

put_parser = reqparse.RequestParser()
put_parser.add_argument('team_leader')
put_parser.add_argument('job')
put_parser.add_argument('work_size')
put_parser.add_argument('collaborators')
post_parser.add_argument('is_finished')
