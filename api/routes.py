import logging
from flask import request, jsonify
from . import app

from .models import Books, Genres, db

logging.basicConfig(level=logging.INFO)

books = [
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "fantasy",
        "year": 1937
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "fantasy",
        "year": 1954
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "dystopian",
        "year": 1949
    },
    {
        "title": "Animal Farm",
        "author": "George Orwell",
        "genre": "satire",
        "year": 1945
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "science fiction",
        "year": 1965
    },
    {
        "title": "Foundation",
        "author": "Isaac Asimov",
        "genre": "science fiction",
        "year": 1951
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "fantasy",
        "year": 1997
    },
    {
        "title": "The Name of the Wind",
        "author": "Patrick Rothfuss",
        "genre": "fantasy",
        "year": 2007
    }
]


@app.route("/")
def start_roure():
    return "<p>Hello, Sanya!</p>"

@app.route('/api/books/', methods=['GET'])
def get_books():

    genre = request.args.get('genre')
    author = request.args.get('author')
    year_from = request.args.get('year_from')
    year_to = request.args.get('year_to')

    filtered_books = books

    if not any([genre, author, year_from, year_to]):
        return jsonify(books)

    filters = {
        "genre": genre,
        "author": author
    }

    for key, value in filters.items():
        if value:
            filtered_books = [
                book for book in filtered_books
                if book[key].lower() == value.lower()
            ]

    if year_from:
        try:
            year_from = int(year_from)

            filtered_books = [
                book for book in filtered_books
                if book["year"] >= year_from
            ]

        except ValueError:
            return jsonify({"error": "year_from must be integer"}), 400

    if year_to:
        try:
            year_to = int(year_to)

            filtered_books = [
                book for book in filtered_books
                if book["year"] <= year_to
            ]

        except ValueError:
            return jsonify({"error": "year_to must be integer"}), 400

    return jsonify(filtered_books)


@app.route('/api/books_db/', methods=['GET'])
def get_books_from_db():

    books = Books.query.all()

    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:id>', methods=['GET'])
def get_information_of_book(id):
    if len(books):
        books_information = books[id]
        return jsonify(books_information)


@app.route('/books_filtred/<string:genre>', methods=['GET'])
def get_genres(genre):
    logging.info(f"Genre filter: {genre}")
    filtered_books = []
    for book in books:
        if book["genre"].lower() == genre.lower():
            filtered_books.append(book)
    return jsonify(filtered_books)

@app.route('/genres')
def get_all_genres():

    genres = Genres.query.all()

    return jsonify(
        [genre.name for genre in genres]
    )


@app.route('/api/books_db/', methods=['POST']) #в таске не был, но добавил для удобства
def add_book():

    data = request.get_json()

    book = Books(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        year=data['year'],
        description=data['description']
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book added"})

