# Dockerfile pour l'API de classification de tickets
# TODO: Compléter et optimiser ce Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# TODO: Installer les dépendances
# Indice : pip install --no-cache-dir -r requirements.txt

# TODO: Copier le code source
# Indice : COPY src/ ./src/

# TODO: Copier le modèle (si chargement depuis fichier local)
# Indice : COPY models/ ./models/

# TODO: Exposer le port de l'API
# Indice : EXPOSE 8000

# TODO: Définir la commande de lancement
# Indice : CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
