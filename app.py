import redis

from flask import Flask

from flask_restful import (
    Resource,
    Api,
    reqparse
)


API_BASE_PATH = '/api/queue'

LIST_NAME = 'message_queue'


app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)

api = Api(app)


class Push(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()        
            parser.add_argument('message', required=False)
            args = parser.parse_args()

            message = args['message']

            if not message:
                return {'message': 'Missing required parameter in \
                    the post body or the query string'}, 404

            cache.rpush(LIST_NAME, message)
         
            return {'message': message}, 200
        except Exception as e:
            return {'message': f'Message not created, {e}'}, 500


class Count(Resource):
    def get(self):
        messages_count = cache.llen(LIST_NAME)

        if messages_count == 0:
            status = 404
        else:
            status = 200

        return {'count': messages_count}, status


class Pop(Resource):
    def post(self):
        messages_count = cache.llen(LIST_NAME)

        if messages_count == 0:
            return {'message': f'Nothing found'}, 500
        else:
            return {'message': str(cache.lpop(LIST_NAME))}, 200


api.add_resource(Push, f'{API_BASE_PATH}/push')
api.add_resource(Count, f'{API_BASE_PATH}/count')
api.add_resource(Pop, f'{API_BASE_PATH}/pop')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)