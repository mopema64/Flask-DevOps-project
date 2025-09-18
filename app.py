from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # Aquí está la salida personalizada con tu nombre
    return "Hola Miguel Angel, ¡bienvenido al mundo de Python en Azure Kubernetes Service!"

if __name__ == "__main__":
    # Obtener el puerto de la variable de entorno, o usar 5000 por defecto
    port = int(os.environ.get('PORT', '5000'))
    app.run(debug=True, host='0.0.0.0', port=port)
