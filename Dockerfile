# Utilise une image officielle de Python
FROM python:3.11-slim

# Installation des dépendances système
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Crée un répertoire pour ton app
WORKDIR /app

# Copie les fichiers requis
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du projet
COPY . .

# Crée le répertoire pour les fichiers statiques et les collecte
RUN mkdir -p staticfiles && python manage.py collectstatic --noinput

# Port d'écoute
EXPOSE 8000

# Commande de lancement
CMD ["gunicorn", "Helldivers_2_Database.wsgi:application", "--bind", "0.0.0.0:8000"]
