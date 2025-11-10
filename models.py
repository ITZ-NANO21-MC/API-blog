from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos

    # Columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    username = db.Column(db.String(50), unique=True, nullable=False)  # Nombre de usuario único
    email = db.Column(db.String(100), unique=True, nullable=False)  # Correo electrónico único
    password_hash = db.Column(db.String(255), nullable=False)  # Hash de la contraseña
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Fecha de creación
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Fecha de actualización

    # Relación uno a muchos: Un usuario puede tener muchos posts
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'    
    
class Post(db.Model):
    __tablename__ = 'posts'  # Nombre de la tabla en la base de datos

    # Columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Clave foránea al usuario
    title = db.Column(db.String(255), nullable=False)  # Título del post
    content = db.Column(db.Text, nullable=False)  # Contenido del post
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Fecha de creación
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Fecha de actualización

    # Relación uno a muchos: Un post puede tener muchos comentarios
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __repr__(self):
        return f'<Post {self.title}>'
    
class Comment(db.Model):
    __tablename__ = 'comments'  # Nombre de la tabla en la base de datos

    # Columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)  # Clave foránea al post
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Clave foránea al usuario
    content = db.Column(db.Text, nullable=False)  # Contenido del comentario
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Fecha de creación

    def __repr__(self):
        return f'<Comment {self.content[:20]}>'