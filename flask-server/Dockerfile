# Gunakan image resmi Python
FROM python:3.9

# Set working directory di dalam container
WORKDIR /app

# Salin file dependensi
COPY requirements.txt .

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Salin aplikasi Flask
COPY . .

# Port yang akan digunakan oleh aplikasi Flask
EXPOSE 5000

# Perintah untuk menjalankan aplikasi saat container dimulai
CMD ["python", "app.py"]
