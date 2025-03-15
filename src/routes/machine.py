from flask import Blueprint, jsonify, request, Response

from src.compose.machine_compose import machine_info_compose

machine_routes_bp = Blueprint("machine_routes", __name__)

@machine_routes_bp.route("/info", methods=["GET"])
def register_user():
    machine_info_controller = machine_info_compose()
    response = machine_info_controller.handler()
    # response = Response(status=200, response={"user": "Thiago Freire"})
    
    return jsonify(response.response), response.status