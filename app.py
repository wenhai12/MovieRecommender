# coding:utf-8

import json
import logging

from flask import Blueprint, Flask, current_app, request, render_template
from engine import RecommendationEngine
from ext import db
from modals import Ratings, Movies, Links, Tags, User

main = Blueprint('main', __name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@main.route('/')
def hello():

    return "h"


@main.route("/<int:user_id>/ratings/top/<int:count>", methods=["GET"])
def top_ratings(user_id, count):
    logger.debug("User %s TOP ratings requested", user_id)
    top_ratings = recommendation_engine.get_top_ratings(user_id, count)
    return json.dumps(top_ratings)


@main.route("/<int:user_id>/ratings/<int:movie_id>", methods=["GET"])
def movie_ratings(user_id, movie_id):
    logger.debug("User %s rating requested for movie %s", user_id, movie_id)
    ratings = recommendation_engine.get_ratings_for_movie_ids(user_id, [movie_id])
    return json.dumps(ratings)


def create_app(spark_context):
    global recommendation_engine

    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    app.register_blueprint(main)

    with app.app_context():
        db.app = app
        db.create_all()

    recommendation_engine = RecommendationEngine(spark_context)

    return app
