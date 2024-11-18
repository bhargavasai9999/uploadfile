from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from ..models import User, db

bp = Blueprint('auth', __name__)

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if not email or not password or not role:
        return jsonify({"error": "Missing required fields"}), 400

    hashed_password = generate_password_hash(password)
    user = User(email=email, password_hash=hashed_password, role=role)
    db.session.add(user)
    db.session.commit()

    verification_url = f"http://localhost:5000/verify/{user.id}"
    return jsonify({"message": "User created", "verification_url": verification_url}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify({"access_token": access_token}), 200
