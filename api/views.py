
from .controllers import get_posts, include_post, delete_post
from flask import Blueprint, request
import json

bp = Blueprint("blog", __name__)


@bp.route("/posts", methods=["GET"])
def get():
    args = dict(request.args)
    data = get_posts(args)
    return json.dumps(data, default=str)


@bp.route("/posts", methods=["POST"])
def post():
    body = dict(request.json)
    data = include_post(body)
    return json.dumps(data, default=str)


@bp.route("/posts", methods=["DELETE"])
def delete():
    args = dict(request.args)
    data = delete_post(args)
    return json.dumps(data, default=str)
