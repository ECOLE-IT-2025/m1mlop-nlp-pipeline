"""
Module d'entraînement et d'évaluation du modèle de classification.

TODO: Implémenter l'entraînement, l'évaluation et le logging MLflow.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, f1_score, accuracy_score
import mlflow
import mlflow.sklearn
import joblib
from loguru import logger

from src.preprocessing import TextPreprocessor, get_tfidf_vectorizer, load_tickets


# ============================================================================
# ÉTAPE 1 : Construction du pipeline ML
# ============================================================================

def build_pipeline(classifier_name: str = "logistic_regression", **kwargs) -> Pipeline:
    """
    Construit un pipeline sklearn complet : preprocessing → vectorisation → classification.

    Args:
        classifier_name: Nom du classifieur à utiliser.
            Options suggérées : "logistic_regression", "random_forest", "svm", "naive_bayes"
        **kwargs: Hyperparamètres du classifieur

    Returns:
        Pipeline sklearn configuré
    """
    # TODO: Implémenter la construction du pipeline
    # 1. Instancier TextPreprocessor()
    # 2. Instancier le vectorizer TF-IDF
    # 3. Instancier le classifieur selon classifier_name
    # 4. Assembler dans un sklearn Pipeline
    #
    # Exemple de structure :
    # pipeline = Pipeline([
    #     ('preprocessor', TextPreprocessor()),
    #     ('vectorizer', get_tfidf_vectorizer()),
    #     ('classifier', VotreClassifieur(**kwargs))
    # ])

    raise NotImplementedError("À compléter : construction du pipeline ML")


# ============================================================================
# ÉTAPE 2 : Entraînement avec MLflow tracking
# ============================================================================

def train_model(
    data_path: str = "data/sample_tickets.csv",
    classifier_name: str = "logistic_regression",
    test_size: float = 0.2,
    random_state: int = 42,
    **kwargs
) -> dict:
    """
    Entraîne le modèle et log les résultats dans MLflow.

    Étapes attendues :
    1. Charger les données
    2. Split train/test
    3. Construire et entraîner le pipeline
    4. Évaluer sur le jeu de test
    5. Logger dans MLflow (paramètres, métriques, modèle)

    Args:
        data_path: Chemin vers les données
        classifier_name: Type de classifieur
        test_size: Proportion du jeu de test
        random_state: Graine aléatoire
        **kwargs: Hyperparamètres du classifieur

    Returns:
        Dictionnaire avec les métriques d'évaluation
    """
    # TODO: Implémenter l'entraînement avec MLflow tracking
    #
    # Indices :
    # - mlflow.start_run() pour démarrer une expérience
    # - mlflow.log_param() pour logger les paramètres
    # - mlflow.log_metric() pour logger les métriques
    # - mlflow.sklearn.log_model() pour sauvegarder le modèle
    #
    # Métriques à logger :
    # - accuracy
    # - f1_score (weighted)
    # - f1_score par catégorie

    raise NotImplementedError("À compléter : entraînement avec MLflow")


# ============================================================================
# ÉTAPE 3 : Évaluation détaillée
# ============================================================================

def evaluate_model(pipeline: Pipeline, X_test, y_test) -> dict:
    """
    Évalue le modèle et retourne un rapport détaillé.

    Args:
        pipeline: Pipeline entraîné
        X_test: Textes de test
        y_test: Labels de test

    Returns:
        Dictionnaire avec les métriques
    """
    # TODO: Implémenter l'évaluation
    # - Prédictions sur X_test
    # - Classification report
    # - Matrice de confusion (optionnel mais recommandé)
    # - F1-score global et par classe

    raise NotImplementedError("À compléter : évaluation du modèle")


# ============================================================================
# ÉTAPE 4 : Sauvegarde et chargement du modèle
# ============================================================================

def save_model(pipeline: Pipeline, filepath: str = "models/model.joblib"):
    """Sauvegarde le pipeline entraîné."""
    joblib.dump(pipeline, filepath)
    logger.info(f"Modèle sauvegardé : {filepath}")


def load_model(filepath: str = "models/model.joblib") -> Pipeline:
    """Charge un pipeline entraîné."""
    pipeline = joblib.load(filepath)
    logger.info(f"Modèle chargé : {filepath}")
    return pipeline


# ============================================================================
# Point d'entrée
# ============================================================================

if __name__ == "__main__":
    """
    Permet de lancer l'entraînement en ligne de commande :
        python -m src.model
    """
    # Configuration MLflow
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("ticket-classification")

    # Entraînement
    results = train_model(
        data_path="data/sample_tickets.csv",
        classifier_name="logistic_regression",
        test_size=0.2,
    )

    print("
=== Résultats ===")
    for metric, value in results.items():
        print(f"{metric}: {value:.4f}")
