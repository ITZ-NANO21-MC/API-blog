from flask import Flask
from models import db
from routes import blog_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blog_personal_2025_02_04'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Registrar las rutas
app.register_blueprint(blog_routes)

if __name__ == '__main__':
    app.run(debug=True)