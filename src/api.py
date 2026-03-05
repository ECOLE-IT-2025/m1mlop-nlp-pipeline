"""
API REST FastAPI pour la classification de tickets support.

TODO: Implémenter les endpoints de prédiction et monitoring.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import time
from loguru import logger

# TODO: Importer votre modèle et les fonctions nécessaires
# from src.model import load_model


# ============================================================================
# Schémas Pydantic
# ============================================================================

class TicketRequest(BaseModel):
    """Schéma de requête pour la classification d'un ticket."""
    text: str = Field(..., min_length=5, description="Texte du ticket support")
    priority: Optional[str] = Field(None, description="Priorité optionnelle")

    class Config:
        json_schema_extra = {
            "example": {
                "text": "L'application plante quand je clique sur exporter",
                "priority": "high"
            }
        }


class TicketResponse(BaseModel):
    """Schéma de réponse avec la prédiction."""
    category: str
    confidence: float
    processing_time_ms: float


class HealthResponse(BaseModel):
    """Schéma de réponse pour le health check."""
    status: str
    model_loaded: bool
    version: str


# ============================================================================
# Application FastAPI
# ============================================================================

app = FastAPI(
    title="Ticket Classifier API",
    description="API de classification automatique de tickets support - M1MLOP",
    version="0.1.0",
)

# Variable globale pour le modèle (chargé au démarrage)
model = None


# ============================================================================
# ÉTAPE 1 : Endpoint de santé (fourni)
# ============================================================================

@app.get("/health", response_model=HealthResponse)
def health_check():
    """Vérifie que l'API est opérationnelle."""
    return HealthResponse(
        status="healthy",
        model_loaded=model is not None,
        version="0.1.0"
    )


# ============================================================================
# ÉTAPE 2 : Endpoint de prédiction
# ============================================================================

@app.post("/predict", response_model=TicketResponse)
def predict(ticket: TicketRequest):
    """
    Classifie un ticket support.

    TODO: Implémenter la logique de prédiction :
    1. Vérifier que le modèle est chargé
    2. Chronomètrer le temps de traitement
    3. Appeler le modèle pour prédire la catégorie
    4. Récupérer le score de confiance (predict_proba)
    5. Retourner la réponse formatée
    """
    # TODO: Implémenter la prédiction
    # Indices :
    # - Vérifier que model is not None, sinon HTTPException(503)
    # - time.time() pour chronométrer
    # - model.predict() et model.predict_proba()

    raise NotImplementedError("À compléter : endpoint de prédiction")


# ============================================================================
# ÉTAPE 3 : Endpoint batch (optionnel mais recommandé)
# ============================================================================

# TODO (Bonus) : Implémenter un endpoint /predict/batch
# qui accepte une liste de tickets et retourne les prédictions


# ============================================================================
# ÉTAPE 4 : Endpoint de métriques Prometheus
# ============================================================================

# TODO : Exposer les métriques pour Prometheus
# Indices :
# - Compteur de requêtes par catégorie prédite
# - Histogramme des temps de réponse
# - Gauge du nombre de requêtes en cours
# - Utiliser prometheus_client


# ============================================================================
# Événements de démarrage
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Charge le modèle au démarrage de l'API."""
    global model

    # TODO: Charger le modèle
    # Option 1 : depuis un fichier local (joblib)
    # Option 2 : depuis MLflow Model Registry
    #
    # Exemple avec MLflow :
    # model = mlflow.sklearn.load_model("models:/ticket-classifier/Production")

    logger.info("API démarrée - En attente du chargement du modèle")
    logger.warning("Modèle non chargé - implémentez le chargement dans startup_event()")


# ============================================================================
# Point d'entrée
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
