# Données

## sample_tickets.csv

Dataset échantillon de 50 tickets support client pour le développement et les tests.

### Colonnes

| Colonne | Type | Description |
|---------|------|-------------|
| `id` | int | Identifiant unique du ticket |
| `text` | string | Texte du ticket (en français) |
| `category` | string | Catégorie cible : `bug`, `feature_request`, `billing`, `account`, `general` |
| `priority` | string | Priorité : `low`, `medium`, `high` |
| `created_at` | date | Date de création |

### Distribution des catégories

- `bug` : 10 tickets
- `feature_request` : 10 tickets
- `billing` : 10 tickets
- `account` : 10 tickets
- `general` : 10 tickets

### Notes

- Ce dataset est un **échantillon** pour le développement.
- Pour l'entraînement, vous devrez **augmenter les données** (data augmentation, paraphrase, etc.) ou utiliser un dataset plus large.
- Les tickets sont rédigés en **français** - adaptez votre pipeline NLP en conséquence.
