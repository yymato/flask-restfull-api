from flask_restful import reqparse

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', required=True)
post_parser.add_argument('about', required=True)
post_parser.add_argument('email', required=True)
post_parser.add_argument('password', required=True)

put_parser = reqparse.RequestParser()
put_parser.add_argument('name')
put_parser.add_argument('about')
put_parser.add_argument('email')
put_parser.add_argument('password')
