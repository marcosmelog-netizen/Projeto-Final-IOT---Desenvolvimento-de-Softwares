from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import os # Necessário para ler as configurações do sistema

# Importando a conexão do banco e os modelos
from models.db import db
from models.user import User
from models.produto import Produto

# Importando os Blueprints (Controladores)
from controllers.auth_controller import auth_bp
from controllers.produto_controller import produto_bp

app = Flask(__name__)

# --- CONFIGURAÇÃO DO BANCO DE DADOS (SQLite vs PostgreSQL) ---

# O Render fornece a URL do banco em uma variável chamada DATABASE_URL
database_url = os.getenv("DATABASE_URL")

if database_url:
    # Pequeno ajuste técnico: O SQLAlchemy exige "postgresql://" mas o Render entrega "postgres://"
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Se estiver rodando no seu PC, ele continuará usando o arquivo local
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- CONFIGURAÇÃO DE SEGURANÇA ---

# Usa uma chave do sistema na nuvem ou uma padrão para testes locais
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "chave-mestra-local-123")

# --- INICIALIZAÇÃO DAS FERRAMENTAS ---

db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# --- REGISTRO DAS ROTAS (MVC) ---

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(produto_bp, url_prefix='/produtos')

# --- CRIAÇÃO AUTOMÁTICA DAS TABELAS ---

with app.app_context():
    db.create_all()

# --- ROTA INICIAL ---

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "ambiente": "producao" if os.getenv("DATABASE_URL") else "desenvolvimento",
        "mensagem": "API de Produtos pronta para o Deploy!"
    })

if __name__ == '__main__':
    # Em produção, o Gunicorn cuidará disso. Localmente, o app roda em modo debug.
    app.run(debug=True)