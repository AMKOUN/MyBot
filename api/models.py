from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Genres(db.Model):
    __tablename__ = 'genres'

    name = db.Column(db.String, primary_key=True, nullable=False)

    # связь: один жанр -> много книг
    books = db.relationship('Books', back_populates='genre_rel')


class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)

    # связь с таблицей genres
    genre = db.Column(
        db.String,
        db.ForeignKey('genres.name'),  # schema.table.column
        nullable=False
    )

    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)

    # обратная связь
    genre_rel = db.relationship('Genres', back_populates='books')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "year": self.year,
            "description": self.description,
        }

