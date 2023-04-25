from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = [
    {'id': 1, 'name': 'Pod Igoto', 'author': 'Ivan Vazov'},
    {'id': 2, 'name': 'Python for Dummies', 'author': 'Stef Maruch'}
]

class Book(BaseModel):
    id: int
    name: str
    author: str

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def create_books(new_book: Book):
    books.append(new_book.dict())
    return new_book


@app.put("/book/{book_id}")
def update_book(book_id: int, update_book: Book):
    for el in books:
        if el.get('id') == book_id:
            el['name'] = update_book.name
            el['author'] = update_book.author
            return {'book_updated': update_book.dict()}
    else:
        return {'book_updated': 'not found'}
