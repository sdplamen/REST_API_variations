"""
This is a sample RESTful API implementation with plain Flask but we will use on top a module called FlaskRESTful
https://flask-restful.readthedocs.io/en/latest/
"""
from flask import Flask, request
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

books = [
    {'id': 1, 'name': 'Pod Igoto', 'author': 'Ivan Vazov'},
    {'id': 2, 'name': 'Python for Dummies', 'author': 'Stef Maruch'}
]

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('author')


class Books(Resource):
    def get(self):
        return books

    def post(self):
        new_book = request.json
        books.append(new_book)
        return {'book_created': new_book}, 201


class Book(Resource):
    def put(self, book_id):
        args = parser.parse_args()
        for book in books:
            if book.get('id') == book_id:
                book['name'] = args['name']
                book['author'] = args['author']
                return {'book_updated': {'name': args['name'], 'author': args['author']}}, 200
            return {'book_updated': 'not found'}, 404


api.add_resource(Books, '/books')
api.add_resource(Book, '/book/<int:book_id>')

if __name__ == '__main__':
    app.run(port=5002, debug=True)
