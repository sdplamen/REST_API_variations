"""
This is a sample RESTful API implementation with plain Flask
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {'id': 1, 'name': 'Pod Igoto', 'author': 'Ivan Vazov'},
    {'id': 2, 'name': 'Python for Dummies', 'author': 'Stef Maruch'}
]


@app.route('/books', methods=['GET', 'POST'])
def books_endpoint():
    if request.method == 'POST':
        new_book = request.json
        books.append(new_book)
        return jsonify({'book_created': new_book}), 201
    else:
        return jsonify(books)


@app.route('/book/<int:book_id>', methods=['PUT'])
def book_endpoint(book_id):
    update_book = request.json
    for book in books:
        if book_id == book.get('id'):
            book['name'] = update_book['name']
            book['author'] = update_book['author']
            return jsonify({'book_updated': update_book}), 200
    return jsonify({'book_updated': 'not found'}), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
