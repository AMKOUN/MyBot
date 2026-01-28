import datetime
from flask import Flask, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from markupsafe import escape


class Books(db.Model):
    __tablename__ = 'books'
    __table_args__ = {'schema': 'books'}
    # TODO: Добавить поля: id (первичный ключ), name (строка), age (целое число)
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "year": self.year,
            "description": self.description,
        }

    # tasks = db.relationship('Task', back_populates='users')


#class Genres(db.Model):
    #__tablename__ = 'genres'
    #__table_args__ = {'schema': 'task'}
    # TODO: Добавить поля: id (первичный ключ), name (строка), age (целое число)
    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String, nullable=False)
    # description = db.Column(db.String)
    # status = db.Column(db.String, nullable=False)
    # done = db.Column(db.Boolean, nullable=False)
    # created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    # updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    # user_id = db.Column(db.Integer, db.ForeignKey('task.users.user_id'))
    # users = db.relationship('User', back_populates='tasks')

    # def __repr__(self):
    #     return f"<Task(id={self.id}, status='{self.status}', description='{self.description}', title='{self.title}', description={self.description})>"

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "title": self.title,
    #         "description": self.description,
    #         "status": self.status,
    #         "done": self.done,
    #         "created_at": self.created_at,
    #         "updated_at": self.updated_at,
    #         "user_id": self.user_id,
    #     }