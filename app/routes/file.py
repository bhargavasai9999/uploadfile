from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import File, User, db
from werkzeug.utils import secure_filename
import os

bp = Blueprint('file', __name__)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    identity = get_jwt_identity()
    if identity['role'] != 'Ops':
        return jsonify({"error": "Only Ops users can upload files"}), 403

    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    encrypted_link = f"http://localhost:3000/download/{filename}"  
    new_file = File(
        uploaded_by=identity['id'],
        file_name=filename,
        file_type=filename.rsplit('.', 1)[1],
        encrypted_link=encrypted_link
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded", "encrypted_link": encrypted_link}), 201
