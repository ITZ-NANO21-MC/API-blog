from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Post, Comment

blog_routes = Blueprint('blog_routes', __name__)

# Función auxiliar para validar datos
def validate_data(data, required_fields):
    if not data:
        return False
    for field in required_fields:
        if field not in data:
            return False
    return True

# Registrar un usuario
@blog_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not validate_data(data, ['username', 'email', 'password']):
        return jsonify({'message': 'Datos incompletos'}), 400

    # Verificar si el usuario o el correo ya existen
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'El nombre de usuario ya existe'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'El correo electrónico ya está registrado'}), 400

    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email
    }), 201

# Iniciar Sesión
@blog_routes.route('/login', methods=['POST'])
def iniciar_sesion():
    data = request.get_json()
    if not validate_data(data, ['email', 'password']):
        return jsonify({'message': 'Datos incompletos'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })
    else:
        return jsonify({'message': 'Correo o contraseña incorrectos'}), 400

# Crear Post
@blog_routes.route('/posts', methods=['POST'])
def crear_post():
    data = request.get_json()
    if not validate_data(data, ['title', 'content', 'user_id']):
        return jsonify({'message': 'Datos incompletos'}), 400

    # Verificar si el usuario existe
    if not User.query.get(data['user_id']):
        return jsonify({'message': 'Usuario no encontrado'}), 404

    post = Post(
        title=data['title'],
        content=data['content'],
        user_id=data['user_id']
    )
    db.session.add(post)
    db.session.commit()
    return jsonify({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'user_id': post.user_id,
        'created_at': post.created_at
    }), 201

# Crear Comentario
@blog_routes.route('/comments', methods=['POST'])
def crear_comentario():
    data = request.get_json()
    if not validate_data(data, ['content', 'user_id', 'post_id']):
        return jsonify({'message': 'Datos incompletos'}), 400

    # Verificar si el usuario y el post existen
    if not User.query.get(data['user_id']):
        return jsonify({'message': 'Usuario no encontrado'}), 404
    if not Post.query.get(data['post_id']):
        return jsonify({'message': 'Post no encontrado'}), 404

    comentario = Comment(
        content=data['content'],
        user_id=data['user_id'],
        post_id=data['post_id']
    )
    db.session.add(comentario)
    db.session.commit()
    return jsonify({
        'id': comentario.id,
        'content': comentario.content,
        'user_id': comentario.user_id,
        'post_id': comentario.post_id,
        'created_at': comentario.created_at
    }), 201

# Obtener todos los posts
@blog_routes.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'user_id': post.user_id,
        'created_at': post.created_at
    } for post in posts])

# Obtener todos los comentarios
@blog_routes.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify([{
        'id': comment.id,
        'content': comment.content,
        'user_id': comment.user_id,
        'post_id': comment.post_id,
        'created_at': comment.created_at
    } for comment in comments])

# Buscar un usuario
@blog_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404

# Buscar un post
@blog_routes.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return jsonify({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'user_id': post.user_id,
            'created_at': post.created_at
        })
    else:
        return jsonify({'message': 'Post no encontrado'}), 404

# Buscar un comentario
@blog_routes.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        return jsonify({
            'id': comment.id,
            'content': comment.content,
            'user_id': comment.user_id,
            'post_id': comment.post_id,
            'created_at': comment.created_at
        })
    else:
        return jsonify({'message': 'Comentario no encontrado'}), 404

# Actualizar un usuario
@blog_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    data = request.get_json()
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })