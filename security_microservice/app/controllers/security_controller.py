from flask import Blueprint, jsonify
from flask import request

from app.services.security_service import SecurityService

security_bp = Blueprint('security_controller', __name__)
security_service = SecurityService()

@security_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = security_service.login(data)
    if result:
        return jsonify({"success": result}), 200
    return jsonify({"success": result}), 502

@security_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(f'data from post:{data}')
    result = security_service.register(data)
    if result:
        return jsonify({"success": result}), 200
    return jsonify({"success": result}), 502
        