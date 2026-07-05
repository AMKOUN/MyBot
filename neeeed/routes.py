from flask import jsonify

from . import app

books = [
    "Изучаем Python",
    "Лёгкий способ выучить Python 3",
    "Основы Python",
    "Автоматизация рутинных задач с помощью Python",
    "Python за 7 дней. Краткий курс для начинающих",
    "Чистый Python. Тонкости программирования для профи",
    "Паттерны разработки на Python",
    "Python-интенсив: 50 быстрых упражнений",
    "Простой Python. Современный стиль программирования",
    "Стандартная библиотека Python 3. Справочник с примерами"
]


@app.route("/")
def start_roure():
    return "<p>Hello, Sanya!</p>"


@app.route('/books/', methods=['GET'])
def get_books():
    # we have to change this function by filtering it for example only titles
    return jsonify(books)


@app.route('/books/<int:id>', methods=['GET'])
def get_information_of_book(id):
    if len(books):
        books_information = books[id]
        return jsonify(books_information)


@app.route('/books/<string:genre>', methods=['GET'])
def get_genres(genre):
    return "<p>Zdes ya nihua ne pridumal(((!</p>"
