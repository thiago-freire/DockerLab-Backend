from flask import Blueprint, jsonify, request, Response
from src.compose.user_compose import create_user_compose, list_user_compose

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/create_user", methods=["POST"])
def register_user():
    
    create_user_controller = create_user_compose()
    response = create_user_controller.handler(request)
    
    return jsonify(response.response), response.status

@user_routes_bp.route("/list", methods=["GET"])
def list_user():
    
    list_user_controller = list_user_compose()
    response = list_user_controller.handler()
    
    return jsonify(response.response), response.status