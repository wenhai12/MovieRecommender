# coding=utf-8
from ext import db


class User(db.Model):
    __tablename__ = 'bk_users2'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


class Ratings(db.Model):
    __tablename__ = 'lens_ratings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    rating = db.Column(db.Float)
    timestamp = db.Column(db.Integer)

    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp


class Tags(db.Model):
    __tablename__ = 'lens_tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    tag = db.Column(db.String(64))
    timestamp = db.Column(db.Integer)

    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp


class Movies(db.Model):
    __tablename__ = 'lens_movies'

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    genres = db.Column(db.String(255))

    def __init__(self, title, genres):
        self.title = title
        self.genres = genres


class Links(db.Model):
    __tablename__ = 'lens_links'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer)
    imdb_id = db.Column(db.String(16))
    tmdb_id = db.Column(db.Integer)

    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id


class Admin(db.Model):
    __tablename__ = 'bk_adminc'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    psword = db.Column(db.String(32))
    email = db.Column(db.String(64))

    def __init__(self, name='anonymous', psword=None, email=None):
        self.name = name
        self.psword = psword
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<admin %r>' % (self.name)

    def get_user(self, name, psword):
        obj = self.query.filter_by(name=name, psword=psword).first()
        return obj
