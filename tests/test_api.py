"""
Tests pour l'API FastAPI.

TODO: Compléter les tests d'intégration de l'API.
"""

import pytest
from fastapi.testclient import TestClient
from src.api import app


client = TestClient(app)


class TestHealthEndpoint:
    """Tests pour l'endpoint /health."""

    def test_health_returns_200(self):
        """Le health check doit retourner 200."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_response_format(self):
        """Le health check doit retourner le bon format."""
        response = client.get("/health")
        data = response.json()
        assert "status" in data
        assert "model_loaded" in data
        assert "version" in data


class TestPredictEndpoint:
    """Tests pour l'endpoint /predict."""

    # TODO: Implémenter les tests de prédiction
    # Indices :
    # - Tester avec un ticket valide
    # - Tester avec un texte trop court (< 5 caractères)
    # - Tester avec un body vide
    # - Tester le format de la réponse (category, confidence, processing_time_ms)
    # - Tester que la confiance est entre 0 et 1
    # - Tester que la catégorie est une des 5 attendues

    def test_predict_valid_ticket(self):
        """Une requête valide doit retourner une prédiction."""
        # TODO: Implémenter
        pass

    def test_predict_empty_text(self):
        """Un texte vide doit retourner une erreur 422."""
        response = client.post("/predict", json={"text": ""})
        assert response.status_code == 422

    def test_predict_missing_text(self):
        """Un body sans champ text doit retourner une erreur 422."""
        response = client.post("/predict", json={})
        assert response.status_code == 422
