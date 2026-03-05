# Architecture Technique

## Vue d'ensemble

Ce document décrit l'architecture cible du système de classification de tickets support.

## Composants

### 1. Pipeline de données

```
Données brutes (CSV) → Preprocessing NLP → Vectorisation → Features
```

Le preprocessing NLP transforme les textes bruts en features exploitables par le modèle ML.

### 2. Pipeline d'entraînement (MLOps)

```
Données → Validation → Preprocessing → Training → Évaluation → Registry
                                                       │
                                                 F1 >= 0.70 ?
                                                  ├── Oui → Deploy
                                                  └── Non → Alert
```

Orchestré par **Apache Airflow**, ce pipeline automatise le cycle de vie du modèle.

### 3. Serving (API REST)

```
Client → FastAPI → Modèle → Prédiction
              ↓
         Prometheus → Grafana
```

L'API expose le modèle via des endpoints REST et les métriques via Prometheus.

### 4. Monitoring

Le monitoring surveille :

- **Performance du modèle** : F1-score, accuracy sur les nouvelles données
- **Data drift** : changement dans la distribution des tickets
- **Latence** : temps de réponse de l'API
- **Volume** : nombre de prédictions par unité de temps

## Stack technique

| Composant | Technologie |
|-----------|-------------|
| Langage | Python 3.11 |
| ML | scikit-learn |
| NLP | spaCy, NLTK |
| API | FastAPI |
| MLOps | MLflow |
| Orchestration | Apache Airflow |
| Containerisation | Docker |
| Déploiement | Kubernetes |
| Monitoring | Prometheus + Grafana |
| Drift detection | Evidently AI |

## Diagramme de flux

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Airflow  │───>│ Training │───>│  MLflow  │───>│  Deploy  │
│   DAG     │    │ Pipeline │    │ Registry │    │  (K8s)   │
└──────────┘    └──────────┘    └──────────┘    └────┬─────┘
                                                      │
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────▼─────┐
│ Grafana  │<───│Prometheus│<───│ Metrics  │<───│ FastAPI  │
│Dashboard │    │          │    │          │    │   API    │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```
