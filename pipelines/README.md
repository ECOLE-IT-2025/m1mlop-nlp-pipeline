# Pipelines d'orchestration

## training_dag.py

DAG Apache Airflow pour l'entraînement automatisé du modèle de classification de tickets.

### Structure du DAG

```
validate_data → preprocess_data → train_model → evaluate_and_decide
                                                       ├── deploy_model → end
                                                       └── notify_failure → end
```

### Exécution locale

Le DAG peut être testé localement avec la stack Docker :

```bash
docker-compose up -d airflow
```

Accéder à l'interface Airflow : http://localhost:8080

### Configuration

Le DAG est programmé pour s'exécuter hebdomadairement (`@weekly`).
Modifiez `schedule_interval` selon vos besoins.
