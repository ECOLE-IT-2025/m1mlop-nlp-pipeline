# M1MLOP - Pipeline MLOps pour Classification de Tickets Support

## Projet Final - MLOps et Natural Language Processing

> **Ecole IT** - Master 1 - Semaine 11 - Module M1MLOP

---

### Contexte

Une entreprise reçoit des centaines de tickets support client chaque jour. Actuellement, le tri est effectué manuellement, ce qui entraîne des délais de traitement et des erreurs d'attribution.

Votre mission : développer un **système de classification automatique** des tickets support en utilisant le NLP, et le déployer en production avec une architecture **MLOps** complète.

### Catégories de tickets

| Catégorie | Description | Exemple |
|-----------|-------------|---------|
| `bug` | Problème technique / dysfonctionnement | "L'application plante au démarrage" |
| `feature_request` | Demande de nouvelle fonctionnalité | "Ajouter un mode sombre" |
| `billing` | Question liée à la facturation | "Ma facture ne correspond pas" |
| `account` | Gestion de compte utilisateur | "Je ne peux pas me connecter" |
| `general` | Question ou demande générale | "Comment exporter mes données ?" |

---

## Architecture cible

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Données   │────>│   Pipeline   │────>│   MLflow     │
│   (CSV)     │     │  Training    │     │   Registry   │
└─────────────┘     └──────────────┘     └──────┬───────┘
                                               │
                    ┌──────────────┐     ┌──────▼───────┐
                    │  Monitoring  │<────│   API REST   │
                    │  (Grafana)   │     │  (FastAPI)   │
                    └──────────────┘     └──────────────┘
```

## Structure du projet

```
m1mlop-nlp-pipeline/
├── src/                    # Code source principal
│   ├── preprocessing.py    # Preprocessing NLP des tickets
│   ├── model.py            # Entraînement et évaluation du modèle
│   ├── api.py              # API REST FastAPI
│   └── monitoring.py       # Utilitaires de monitoring
├── data/                   # Données d'entraînement
│   └── sample_tickets.csv  # Dataset échantillon
├── pipelines/              # Orchestration (Airflow DAG)
│   └── training_dag.py     # DAG d'entraînement automatisé
├── mlflow/                 # Configuration MLflow
│   └── MLproject           # Fichier projet MLflow
├── kubernetes/             # Configs de déploiement K8s
│   ├── deployment.yaml     # Deployment du modèle
│   └── service.yaml        # Service exposé
├── monitoring/             # Stack de monitoring
│   ├── grafana/            # Dashboards Grafana
│   └── prometheus/         # Configuration Prometheus
├── tests/                  # Tests unitaires et d'intégration
├── notebooks/              # Notebooks d'exploration
├── docs/                   # Documentation technique
├── Dockerfile              # Image Docker de l'API
├── docker-compose.yml      # Stack locale complète
└── requirements.txt        # Dépendances Python
```

---

## Getting Started

### 1. Cloner le repo et installer les dépendances

```bash
git clone https://github.com/ECOLE-IT-2025/m1mlop-nlp-pipeline.git
cd m1mlop-nlp-pipeline
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Explorer les données

```bash
jupyter notebook notebooks/exploration.ipynb
```

### 3. Lancer MLflow

```bash
mlflow ui --port 5000
```

### 4. Lancer la stack Docker

```bash
docker-compose up -d
```

---

## Travail attendu

### Phase 1 - Preprocessing et Modèle (Jour 4-5 matin)

- [ ] Compléter `src/preprocessing.py` : pipeline de nettoyage et vectorisation
- [ ] Compléter `src/model.py` : entraînement, évaluation et sauvegarde
- [ ] Logger les expériences avec MLflow (métriques, paramètres, artefacts)
- [ ] Atteindre un F1-score minimum de **0.70** sur le jeu de test

### Phase 2 - API et Déploiement (Jour 5)

- [ ] Compléter `src/api.py` : endpoints de prédiction et santé
- [ ] Finaliser le `Dockerfile` pour containeriser l'API
- [ ] Configurer le `docker-compose.yml` pour la stack complète
- [ ] Écrire les tests dans `tests/`

### Phase 3 - MLOps et Monitoring (Jour 5)

- [ ] Compléter le DAG Airflow dans `pipelines/training_dag.py`
- [ ] Configurer le monitoring avec Prometheus et Grafana
- [ ] Implémenter la détection de drift dans `src/monitoring.py`
- [ ] Compléter les manifestes Kubernetes

### Bonus

- [ ] Implémenter le A/B testing entre deux versions de modèle
- [ ] Ajouter un système de rollback automatique
- [ ] Mettre en place un pipeline CI/CD (`.github/workflows/`)

---

## Critères d'évaluation

| Critère | Points | Description |
|---------|--------|-------------|
| Preprocessing NLP | /4 | Qualité du pipeline de nettoyage et tokenisation |
| Modèle ML | /4 | Performance, choix du modèle, hyperparamètres |
| MLflow tracking | /3 | Logging des expériences, registre de modèles |
| API REST | /3 | Endpoints fonctionnels, gestion d'erreurs |
| Docker | /2 | Containerisation correcte et fonctionnelle |
| Monitoring | /2 | Métriques exposées et dashboard |
| Code quality | /2 | Tests, documentation, structure du code |
| **Total** | **/20** | |

---

## Ressources utiles

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [scikit-learn Pipelines](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
- [Apache Airflow](https://airflow.apache.org/docs/)
- [Evidently AI - ML Monitoring](https://docs.evidentlyai.com/)

---

*Ecole IT - M1MLOP - MLOps et Natural Language Processing - 2025-2026*
