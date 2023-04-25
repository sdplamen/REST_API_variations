"""
This is a sample REST API implementation with  Flask but we will use on top a module called FlaskRESTPlus
https://flask-restplus.readthedocs.io/en/stable/index.html
Abond this module
Just for illustration purposes
USE FLASK RESTX
"""
from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

books = [
    {'id': 1, 'name': 'Pod Igoto', 'author': 'Ivan Vazov'},
    {'id': 2, 'name': 'Python for Dummies', 'author': 'Stef Maruch'}
]


api.route('/books')
class Books(Resource):

    def get(self):
        return books

    def post(self):
        pass


if __name__ == '__main__':
    app.run(port=5003, debug=True)
