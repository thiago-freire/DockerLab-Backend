from flask import Blueprint, jsonify, request, Response

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/create", methods=["POST"])
def register_user():
    # create_user_controller = create_user_compose()
    # response = create_user_controller.handler(request)
    response = Response(status=200, response={"user": "Thiago Freire"})
    
    return jsonify(response.response), response.status