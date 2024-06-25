# Gunakan base image Python 3.12
FROM python:3.12

# Set environment variables untuk Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Buat direktori untuk aplikasi
RUN mkdir /app

# Set direktori kerja di dalam container
WORKDIR /app

# Copy requirements.txt dan instal dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy kode aplikasi Django Anda ke dalam container
COPY . /app/

# Expose port 5000 untuk akses web (jika diperlukan)
EXPOSE 5000

# Jalankan server web menggunakan manage.py
CMD 
    