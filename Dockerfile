Usa una imagen base oficial de Python
FROM python:3.9-slim

Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

Copia el archivo de requisitos y los instala
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

Copia el código de la aplicación
COPY . .

Expone el puerto que la aplicación usará
EXPOSE 5000

Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]