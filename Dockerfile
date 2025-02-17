# Välj en officiell Python-bild från Docker Hub som bas
FROM python:3.9-slim

# Sätt arbetskatalogen där appen kommer att ligga
WORKDIR /app

# Kopiera requirements.txt för att installera beroenden
COPY requirements.txt /app/

# Installera alla Python-beroenden i requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera hela applikationen till arbetskatalogen i containern
COPY . /app/

# Exponera den port som applikationen ska köras på (standard är 5000 för Flask)
EXPOSE 5000

# Kommandot för att köra appen med Gunicorn (Flask appen ligger i app.py och heter app)
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
