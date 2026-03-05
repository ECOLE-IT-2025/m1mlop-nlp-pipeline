"""
Tests unitaires pour le module de preprocessing.

Certains tests sont fournis, d'autres sont à compléter.
"""

import pytest
from src.preprocessing import clean_text, remove_stopwords, TextPreprocessor, load_tickets


class TestCleanText:
    """Tests pour la fonction clean_text."""

    def test_lowercase(self):
        """Le texte doit être converti en minuscules."""
        result = clean_text("BONJOUR LE MONDE")
        assert result == result.lower()

    def test_remove_urls(self):
        """Les URLs doivent être supprimées."""
        result = clean_text("Visitez https://example.com pour plus d'infos")
        assert "https" not in result
        assert "example.com" not in result

    def test_empty_string(self):
        """Une chaîne vide doit retourner une chaîne vide."""
        assert clean_text("") == ""

    def test_none_input(self):
        """None doit retourner une chaîne vide."""
        assert clean_text(None) == ""

    def test_special_characters(self):
        """Les caractères spéciaux doivent être supprimés."""
        result = clean_text("Hello @world! #test $100")
        assert "@" not in result
        assert "#" not in result

    # TODO: Ajouter d'autres tests
    # - test_multiple_spaces : les espaces multiples doivent être réduits
    # - test_numbers : les nombres doivent-ils être gardés ?
    # - test_accents : selon votre stratégie


class TestTextPreprocessor:
    """Tests pour le transformer TextPreprocessor."""

    def test_fit_returns_self(self):
        """fit() doit retourner self."""
        preprocessor = TextPreprocessor()
        result = preprocessor.fit(["test"])
        assert result is preprocessor

    # TODO: Ajouter des tests pour transform()
    # - test_transform_list : transformer une liste de textes
    # - test_transform_series : transformer une pd.Series
    # - test_output_type : vérifier le type de sortie


class TestLoadTickets:
    """Tests pour le chargement des données."""

    def test_load_sample(self):
        """Le fichier sample doit se charger correctement."""
        df = load_tickets("data/sample_tickets.csv")
        assert len(df) == 50
        assert "text" in df.columns
        assert "category" in df.columns

    def test_categories(self):
        """Les 5 catégories attendues doivent être présentes."""
        df = load_tickets("data/sample_tickets.csv")
        expected = {"bug", "feature_request", "billing", "account", "general"}
        assert set(df["category"].unique()) == expected
