from flask import Blueprint, Response, request

from oauth_flask_jwt import authentication

auth = Blueprint("auth", __name__, url_prefix="/")


@auth.route("/register", methods=["POST", "DELETE"])
def register() -> Response:
    if request.method == "POST":
        authentication.register_client()
        return Response()
    elif request.method == "DELETE":
        raise NotImplementedError
    else:
        raise AssertionError("unexpected method")


@auth.route("/auth", methods=["POST"])
def authenticate() -> Response:
    authentication.authenticate()
    return Response()


@auth.route("/verify", methods=["POST"])
def verify() -> Response:
    authentication.verify_token()
    return Response()


@auth.route("/logout", methods=["POST"])
def logout() -> Response:
    authentication.invalidate_token()
    return Response()
