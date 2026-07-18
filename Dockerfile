# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los requerimientos y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de tu código
COPY . .

# Comando para ejecutar tu app de Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.maxUploadSize=1024"]