"""
DAG Apache Airflow pour l'entraînement automatisé du modèle.

TODO: Compléter les tâches du DAG pour automatiser le pipeline ML.

Ce DAG orchestre les étapes suivantes :
1. Validation des données
2. Preprocessing
3. Entraînement du modèle
4. Évaluation
5. Enregistrement dans MLflow
6. Déploiement (si les métriques sont satisfaisantes)
"""

from datetime import datetime, timedelta

# Note : Airflow n'a pas besoin d'être installé pour écrire le DAG.
# Il sera exécuté dans un environnement Airflow (docker-compose).
try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator, BranchPythonOperator
    from airflow.operators.empty import EmptyOperator
    AIRFLOW_AVAILABLE = True
except ImportError:
    AIRFLOW_AVAILABLE = False


# ============================================================================
# Configuration du DAG
# ============================================================================

default_args = {
    "owner": "mlops-team",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# ============================================================================
# Fonctions des tâches
# ============================================================================

def validate_data(**kwargs):
    """
    Tâche 1 : Valide la qualité des données d'entraînement.

    Vérifications attendues :
    - Le fichier existe et n'est pas vide
    - Les colonnes requises sont présentes
    - Pas de valeurs manquantes critiques
    - Distribution des classes équilibrée
    """
    # TODO: Implémenter la validation des données
    # Indice : charger le CSV et vérifier les contraintes
    # Indice : lever une exception si les données sont invalides

    raise NotImplementedError("À compléter : validation des données")


def preprocess_data(**kwargs):
    """
    Tâche 2 : Applique le preprocessing NLP aux données.

    Utilise le TextPreprocessor de src/preprocessing.py
    et sauvegarde les données preprocessées.
    """
    # TODO: Implémenter le preprocessing
    # Indice : utiliser les XCom d'Airflow pour passer des données entre tâches
    # kwargs['ti'].xcom_push(key='data_path', value='...')

    raise NotImplementedError("À compléter : preprocessing des données")


def train_model(**kwargs):
    """
    Tâche 3 : Entraîne le modèle et log dans MLflow.

    Utilise la fonction train_model() de src/model.py
    """
    # TODO: Implémenter l'entraînement
    # Indice : récupérer les données via XCom
    # data_path = kwargs['ti'].xcom_pull(key='data_path')

    raise NotImplementedError("À compléter : entraînement du modèle")


def evaluate_and_decide(**kwargs):
    """
    Tâche 4 : Évalue le modèle et décide du déploiement.

    Retourne l'ID de la tâche suivante :
    - 'deploy_model' si F1-score >= 0.70
    - 'notify_failure' sinon
    """
    # TODO: Implémenter l'évaluation et la décision
    # C'est un BranchPythonOperator : retourner le task_id de la branche choisie

    raise NotImplementedError("À compléter : évaluation et décision")


def deploy_model(**kwargs):
    """
    Tâche 5a : Déploie le modèle validé.

    Actions :
    - Promouvoir le modèle en "Production" dans MLflow
    - Mettre à jour l'API avec le nouveau modèle
    """
    # TODO: Implémenter le déploiement

    raise NotImplementedError("À compléter : déploiement du modèle")


def notify_failure(**kwargs):
    """
    Tâche 5b : Notifie l'échec de l'entraînement.
    """
    # TODO: Implémenter la notification (log, email, slack, etc.)

    raise NotImplementedError("À compléter : notification d'échec")


# ============================================================================
# Définition du DAG
# ============================================================================

if AIRFLOW_AVAILABLE:
    with DAG(
        dag_id="ticket_classifier_training",
        default_args=default_args,
        description="Pipeline d'entraînement automatisé pour le classifieur de tickets",
        schedule_interval="@weekly",  # Ré-entraînement hebdomadaire
        start_date=datetime(2025, 1, 1),
        catchup=False,
        tags=["mlops", "nlp", "m1mlop"],
    ) as dag:

        # TODO: Définir les tâches et leurs dépendances
        #
        # Structure attendue :
        #
        # validate → preprocess → train → evaluate_and_decide
        #                                       ├── deploy_model → end
        #                                       └── notify_failure → end
        #
        # Exemple :
        # task_validate = PythonOperator(
        #     task_id='validate_data',
        #     python_callable=validate_data,
        # )

        pass  # TODO: Remplacer par la définition des tâches
