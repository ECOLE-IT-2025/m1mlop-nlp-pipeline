"""
Module de monitoring et détection de drift pour le modèle ML.

TODO: Implémenter les métriques de monitoring et la détection de drift.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime
from loguru import logger


# ============================================================================
# ÉTAPE 1 : Collecte des prédictions
# ============================================================================

class PredictionLogger:
    """
    Collecte et stocke les prédictions pour le monitoring.

    Enregistre chaque prédiction avec son timestamp, le texte d'entrée,
    la catégorie prédite et le score de confiance.
    """

    def __init__(self):
        self.predictions: List[Dict] = []

    def log_prediction(self, text: str, category: str, confidence: float):
        """
        Enregistre une prédiction.

        Args:
            text: Texte du ticket
            category: Catégorie prédite
            confidence: Score de confiance
        """
        self.predictions.append({
            "timestamp": datetime.now().isoformat(),
            "text_length": len(text),
            "category": category,
            "confidence": confidence,
        })

    def get_recent_predictions(self, n: int = 100) -> pd.DataFrame:
        """Retourne les n dernières prédictions."""
        return pd.DataFrame(self.predictions[-n:])


# ============================================================================
# ÉTAPE 2 : Détection de drift
# ============================================================================

def detect_distribution_drift(
    reference_distribution: Dict[str, float],
    current_distribution: Dict[str, float],
    threshold: float = 0.1
) -> Dict:
    """
    Détecte un drift dans la distribution des catégories prédites.

    Compare la distribution actuelle des prédictions avec une distribution
    de référence (celle observée lors de l'entraînement).

    Args:
        reference_distribution: Distribution de référence (ex: {"bug": 0.2, "billing": 0.2, ...})
        current_distribution: Distribution actuelle des prédictions
        threshold: Seuil de détection du drift

    Returns:
        Dictionnaire avec :
        - drift_detected (bool) : si un drift a été détecté
        - drift_score (float) : score de drift
        - details (dict) : détails par catégorie
    """
    # TODO: Implémenter la détection de drift
    # Suggestions d'approches :
    # - Divergence de Kullback-Leibler (KL)
    # - Test de Kolmogorov-Smirnov
    # - Population Stability Index (PSI)
    # - Simple comparaison des proportions

    raise NotImplementedError("À compléter : détection de drift de distribution")


def detect_confidence_drift(
    reference_mean_confidence: float,
    current_confidences: List[float],
    threshold: float = 0.05
) -> Dict:
    """
    Détecte un drift dans les scores de confiance du modèle.

    Une baisse significative de la confiance moyenne peut indiquer
    que le modèle rencontre des données différentes de l'entraînement.

    Args:
        reference_mean_confidence: Confiance moyenne de référence
        current_confidences: Scores de confiance récents
        threshold: Seuil de détection

    Returns:
        Dictionnaire avec les résultats de détection
    """
    # TODO: Implémenter la détection de drift de confiance

    raise NotImplementedError("À compléter : détection de drift de confiance")


# ============================================================================
# ÉTAPE 3 : Alertes
# ============================================================================

def check_alerts(prediction_logger: PredictionLogger, config: dict = None) -> List[Dict]:
    """
    Vérifie les conditions d'alerte et retourne les alertes actives.

    Conditions d'alerte possibles :
    - Confiance moyenne < seuil
    - Distribution des catégories anormale
    - Volume de prédictions anormal
    - Temps de réponse élevé

    Args:
        prediction_logger: Logger de prédictions
        config: Configuration des seuils d'alerte

    Returns:
        Liste des alertes actives
    """
    # TODO: Implémenter le système d'alertes

    raise NotImplementedError("À compléter : système d'alertes")
