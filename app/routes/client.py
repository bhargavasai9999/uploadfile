from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import File

bp = Blueprint('client', __name__)

@bp.route('/download/<file_id>', methods=['GET'])
@jwt_required()
def download_file(file_id):
    identity = get_jwt_identity()
    if identity['role'] != 'Client':
        return jsonify({"error": "Only Client users can download files"}), 403

    file = File.query.get(file_id)
    if not file:
        return jsonify({"error": "File not found"}), 404

    return jsonify({"download_link": file.encrypted_link}), 200
