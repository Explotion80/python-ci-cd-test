# Wybór oficjalnego obrazu Pythona
FROM python:3.11-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie plików aplikacji
COPY requirements.txt .
COPY app.py .

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Komenda domyślna przy uruchomieniu kontenera
CMD ["python", "app.py"]
