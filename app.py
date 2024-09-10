import os
from flask import Flask
from src.routers import user

app = Flask(__name__)

app.register_blueprint(user.main, url_prefix='/user')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa la variable de entorno PORT o el puerto 5000 por defecto
    app.run(host='0.0.0.0', port=port)
