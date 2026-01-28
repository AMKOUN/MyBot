from . import app
from .models import Books
from flask import url_for, request, jsonify

@app.route('/books/', methods=['GET'])
def get_books():
    # we have to change this function by filtering it for example only titles
    books = Books.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:id>', methods=['GET'])
def get_information_of_book(id):
    books_information = Books.query.filter_by(id=id).all()
    return jsonify([book.to_dict() for book in books_information]), 200

@app.route('/books/<str:genre>', methods=['GET'])
def get_genres(genre):
    genres = Books.query.filter_by(genre=genre).all()
    return jsonify([genre.to_dict() for genre in genres]), 200

