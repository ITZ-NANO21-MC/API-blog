# API de Blog Personal 📝

Esta es una API simple construida con Flask que permite gestionar un blog personal. Incluye funcionalidades para crear usuarios, publicar posts, agregar comentarios y más.

---

## Características 🚀

- **Gestión de usuarios:** Registro, inicio de sesión y actualización de perfiles.
- **Publicación de posts:** Crear, leer y listar posts.
- **Comentarios:** Agregar comentarios a los posts.
- **Base de datos:** Usa SQLite para almacenar datos.
- **Validaciones:** Validación de entradas y manejo de errores.
- **RESTful:** Diseñada siguiendo las mejores prácticas REST.

---

## Requisitos 📋

- Python 3.8 o superior.
- Flask y SQLAlchemy (instalados automáticamente con `requirements.txt`).

---

## Instalación 🛠️

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/blog-personal-api.git
   cd blog-personal-api
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicia la aplicación:

   ```bash
   python app.py
   ```

   La API estará disponible en `http://127.0.0.1:5000`.

---

## Uso 🚀

### Endpoints Disponibles

#### Usuarios
- **Registrar un usuario:**
  ```
  POST /users
  ```
  **Body:**
  ```json
  {
    "username": "john",
    "email": "john@example.com",
    "password": "1234"
  }
  ```

- **Iniciar sesión:**
  ```
  POST /login
  ```
  **Body:**
  ```json
  {
    "email": "john@example.com",
    "password": "1234"
  }
  ```

- **Obtener un usuario por ID:**
  ```
  GET /users/<int:user_id>
  ```

- **Actualizar un usuario:**
  ```
  PUT /users/<int:user_id>
  ```
  **Body:**
  ```json
  {
    "username": "john_doe",
    "email": "john.doe@example.com"
  }
  ```

#### Posts
- **Crear un post:**
  ```
  POST /posts
  ```
  **Body:**
  ```json
  {
    "title": "Mi primer post",
    "content": "Hola mundo",
    "user_id": 1
  }
  ```

- **Obtener todos los posts:**
  ```
  GET /posts
  ```

- **Obtener un post por ID:**
  ```
  GET /posts/<int:post_id>
  ```

#### Comentarios
- **Crear un comentario:**
  ```
  POST /comments
  ```
  **Body:**
  ```json
  {
    "content": "¡Gran post!",
    "user_id": 1,
    "post_id": 1
  }
  ```

- **Obtener todos los comentarios:**
  ```
  GET /comments
  ```

- **Obtener un comentario por ID:**
  ```
  GET /comments/<int:comment_id>
  ```

---

## Estructura del Proyecto 📂

```
/blog-personal-api
│
├── app.py                # Punto de entrada de la aplicación
├── routes.py             # Definición de las rutas
├── models.py             # Modelos de la base de datos (User, Post, Comment)
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Este archivo
└── database.db           # Base de datos SQLite (se crea automáticamente)
```

---

## Ejemplos de Respuestas

### Respuesta Exitosa (Registro de Usuario)
```json
{
  "id": 1,
  "username": "john",
  "email": "john@example.com"
}
```

### Error (Datos Incompletos)
```json
{
  "message": "Datos incompletos"
}
```

### Error (Usuario No Encontrado)
```json
{
  "message": "Usuario no encontrado"
}
```

---

## Contribuir 🤝

¡Las contribuciones son bienvenidas! Si deseas mejorar esta API, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

## Licencia 📄

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---



