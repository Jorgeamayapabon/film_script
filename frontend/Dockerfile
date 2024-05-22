# Dockerfile para el frontend de Flet

# Utilizar una imagen base de Python
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto, exceptuando los definidos en .dockerignore
COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8550

# Comando para correr la aplicación
CMD ["flet run --web -p 8550", "main.py"]