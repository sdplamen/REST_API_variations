"""
This is a sample REST API implementation with Flask but we will use on top a module called Flask RestX
https://flask-restx.readthedocs.io/en/latest/
"""

from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

books = [
    {'id': 1, 'name': 'Pod Igoto', 'author': 'Ivan Vazov'},
    {'id': 2, 'name': 'Python for Dummies', 'author': 'Stef Maruch'}
]


@api.route('/books')
class Books(Resource):
    def get(self):
        return books, 200

    def post(self):
        book = {
            'id': api.payload['id'],
            'name': api.payload['name'],
            'author': api.payload['author']
        }
        books.append(book)
        return book, 201

@api.route('/book/<int:book_id>')
class Book(Resource):
    def put(self, book_id):
        for book in books:
            if book.get('id') == book_id:
                book['name'] = api.payload['name']
                book['author'] = api.payload['author']
                return {'book_updated': {'name': api.payload['name'], 'author': api.payload['author']}}, 200
        return {'book_updated': 'not found'}, 404


if __name__ == '__main__':
    app.run(port=5004, debug=True)
