from flask import Blueprint, request, jsonify
from models.db import db
from models.user import User
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

# ROTA DE CADASTRO
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"erro": "Usuário já existe"}), 400

    hashed_pwd = generate_password_hash(data['password']).decode('utf-8')
    
    new_user = User(
        username=data['username'],
        password=hashed_pwd,
        role=data.get('role', 'comum')
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"mensagem": "Usuário criado com sucesso!"}), 201

# ROTA DE LOGIN
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        # Mudança importante: identity agora é apenas o username (string)
        token = create_access_token(identity=user.username)
        return jsonify({"token": token}), 200
    
    return jsonify({"erro": "Credenciais inválidas"}), 401