# Projeto Final IoT - Desenvolvimento de Softwares

Este projeto consiste em um sistema web completo desenvolvido com **Flask**, estruturado no padrão **MVC (Model-View-Controller)**. Ele oferece uma API robusta para gerenciamento de registros (CRUD) com foco em persistência de dados e segurança, servindo como backend para aplicações de Internet das Coisas (IoT).

## 🌐 Link do Projeto em Produção
O deploy foi realizado na plataforma Render e pode ser acessado em:
[https://projeto-final-iot-desenvolvimento-de.onrender.com](https://projeto-final-iot-desenvolvimento-de.onrender.com)

## 🚀 Funcionalidades Principais
*   **CRUD Completo**: Permite criar, listar, editar e excluir registros de forma eficiente.
*   **Autenticação e Autorização**:
    *   Implementação de login com **Hashing de Senha** seguro (Bcrypt).
    *   Geração de **Tokens JWT** para acesso a rotas protegidas.
    *   Níveis de acesso distintos: **Admin** (total) e **Usuário comum** (limitado).
*   **Padrão MVC**:
    *   **Models**: Mapeamento de banco de dados com **SQLAlchemy**.
    *   **Views**: Respostas estruturadas em formato **JSON**.
    *   **Controllers**: Lógica de rotas e regras de negócio integradas.
*   **Persistência de Dados**: Integração com banco de dados **PostgreSQL** para ambiente de produção.

## 🛠️ Tecnologias Utilizadas
*   **Linguagem**: Python 3.10+
*   **Framework Web**: Flask
*   **Banco de Dados**: PostgreSQL / SQLAlchemy
*   **Servidor de Produção**: Gunicorn
*   **Plataforma de Nuvem**: Render

## ⚙️ Como Executar Localmente
1.  Clone o repositório:
    ```bash
    git clone [https://github.com/marcosmelog-netizen/Projeto-Final-IOT---Desenvolvimento-de-Softwares.git](https://github.com/marcosmelog-netizen/Projeto-Final-IOT---Desenvolvimento-de-Softwares.git)
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
