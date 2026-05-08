from flask import Blueprint, request, jsonify
from models.db import db
from models.produto import Produto
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

produto_bp = Blueprint('produto', __name__)

# CRIAR PRODUTO
@produto_bp.route('/', methods=['POST'])
@jwt_required()
def create_produto():
    data = request.get_json()
    novo_produto = Produto(
        nome=data['nome'],
        preco=data['preco'],
        descricao=data.get('descricao', '')
    )
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({"mensagem": "Produto criado!"}), 201

# LISTAR PRODUTOS
@produto_bp.route('/', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    output = [{"id": p.id, "nome": p.nome, "preco": p.preco} for p in produtos]
    return jsonify(output)

# EDITAR PRODUTO
@produto_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_produto(id):
    data = request.get_json()
    produto = Produto.query.get_or_404(id)
    
    produto.nome = data.get('nome', produto.nome)
    produto.preco = data.get('preco', produto.preco)
    
    db.session.commit()
    return jsonify({"mensagem": "Produto atualizado!"})

# EXCLUIR PRODUTO (Somente Admin)
@produto_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_produto(id):
    # Recupera o nome do usuário do Token
    username_atual = get_jwt_identity()
    
    # Busca o usuário no banco para validar a Role
    user = User.query.filter_by(username=username_atual).first()
    
    if not user or user.role != 'admin':
        return jsonify({"erro": "Acesso negado. Somente administradores podem excluir."}), 403
    
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return jsonify({"mensagem": "Produto removido com sucesso!"})