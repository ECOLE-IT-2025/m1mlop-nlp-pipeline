"""
Module de preprocessing NLP pour les tickets support.

TODO: Implémenter les fonctions de nettoyage et de vectorisation du texte.
Les étudiants doivent compléter les fonctions marquées TODO.
"""

import re
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer


# ============================================================================
# ÉTAPE 1 : Nettoyage du texte
# ============================================================================

def clean_text(text: str) -> str:
    """
    Nettoie un texte brut de ticket support.

    Opérations attendues :
    - Conversion en minuscules
    - Suppression des URLs
    - Suppression des caractères spéciaux (garder lettres, chiffres, espaces)
    - Suppression des espaces multiples
    - Suppression des accents (optionnel, selon votre stratégie)

    Args:
        text: Texte brut du ticket

    Returns:
        Texte nettoyé
    """
    if not isinstance(text, str):
        return ""

    # TODO: Implémenter le nettoyage du texte
    # Indice : utilisez re.sub() pour les regex
    # Indice : .lower() pour les minuscules

    raise NotImplementedError("À compléter : nettoyage du texte")


def remove_stopwords(text: str, language: str = "french") -> str:
    """
    Supprime les stopwords du texte.

    Args:
        text: Texte nettoyé
        language: Langue des stopwords

    Returns:
        Texte sans stopwords
    """
    # TODO: Implémenter la suppression des stopwords
    # Indice : utilisez nltk.corpus.stopwords ou spacy

    raise NotImplementedError("À compléter : suppression des stopwords")


# ============================================================================
# ÉTAPE 2 : Tokenisation et Lemmatisation
# ============================================================================

def tokenize_and_lemmatize(text: str) -> str:
    """
    Tokenise et lemmatise le texte.

    Args:
        text: Texte nettoyé

    Returns:
        Texte lemmatisé
    """
    # TODO: Implémenter la tokenisation et la lemmatisation
    # Indice : utilisez spaCy avec le modèle français (fr_core_news_sm)
    # Indice : token.lemma_ pour obtenir le lemme

    raise NotImplementedError("À compléter : tokenisation et lemmatisation")


# ============================================================================
# ÉTAPE 3 : Pipeline de preprocessing sklearn-compatible
# ============================================================================

class TextPreprocessor(BaseEstimator, TransformerMixin):
    """
    Transformer sklearn-compatible pour le preprocessing du texte.

    S'intègre dans un sklearn.pipeline.Pipeline.

    Exemple d'utilisation :
        pipeline = Pipeline([
            ('preprocessor', TextPreprocessor()),
            ('vectorizer', TfidfVectorizer()),
            ('classifier', LogisticRegression())
        ])
    """

    def __init__(self, remove_stops: bool = True, lemmatize: bool = True):
        self.remove_stops = remove_stops
        self.lemmatize = lemmatize

    def fit(self, X, y=None):
        """Fit - rien à apprendre pour le preprocessing."""
        return self

    def transform(self, X, y=None):
        """
        Applique le preprocessing sur une série de textes.

        Args:
            X: pd.Series ou liste de textes

        Returns:
            Liste de textes preprocessés
        """
        # TODO: Implémenter la transformation
        # 1. Appliquer clean_text() sur chaque texte
        # 2. Si self.remove_stops : appliquer remove_stopwords()
        # 3. Si self.lemmatize : appliquer tokenize_and_lemmatize()

        raise NotImplementedError("À compléter : pipeline de preprocessing")


# ============================================================================
# ÉTAPE 4 : Vectorisation (fourni comme exemple)
# ============================================================================

def get_tfidf_vectorizer(max_features: int = 5000, ngram_range: tuple = (1, 2)) -> TfidfVectorizer:
    """
    Retourne un vectorizer TF-IDF configuré.

    Cette fonction est fournie comme point de départ.
    Vous pouvez la modifier ou utiliser d'autres approches
    (Word2Vec, FastText, sentence-transformers, etc.)

    Args:
        max_features: Nombre maximum de features
        ngram_range: Range des n-grammes

    Returns:
        TfidfVectorizer configuré
    """
    return TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        sublinear_tf=True,
        strip_accents='unicode'
    )


# ============================================================================
# Utilitaire : chargement des données
# ============================================================================

def load_tickets(filepath: str = "data/sample_tickets.csv") -> pd.DataFrame:
    """
    Charge le dataset de tickets.

    Args:
        filepath: Chemin vers le fichier CSV

    Returns:
        DataFrame avec les tickets
    """
    df = pd.read_csv(filepath)
    print(f"Dataset chargé : {len(df)} tickets, {df['category'].nunique()} catégories")
    print(f"Distribution :\n{df['category'].value_counts()}")
    return df
