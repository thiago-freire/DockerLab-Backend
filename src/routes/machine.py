from flask import Blueprint, jsonify, request, Response

from src.compose.machine_compose import machine_info_compose, create_machine_compose, list_machine_compose

machine_routes_bp = Blueprint("machine_routes", __name__)

@machine_routes_bp.route("/info", methods=["GET"])
def machine_info():
    
    machine_info_controller = machine_info_compose()
    response = machine_info_controller.handler()
    
    return jsonify(response.response), response.status

@machine_routes_bp.route("/create", methods=["POST"])
def register_machine():
    
    create_machine_controller = create_machine_compose()
    response = create_machine_controller.handler(request)
    
    return jsonify(response.response), response.status

@machine_routes_bp.route("/list", methods=["GET"])
def list_machine():
    
    list_machine_controller = list_machine_compose()
    response = list_machine_controller.handler()
    
    return jsonify(response.response), response.status