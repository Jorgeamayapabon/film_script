# Dockerfile para el backend de Django

# Utilizar una imagen base de Python
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto, exceptuando los definidos en .dockerignore
COPY .. .

# Exponer el puerto en el que correrá el servidor
EXPOSE 8000

# Comando para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]