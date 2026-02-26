# python-learning

## Environnement
- Gestionnaire : `uv`
- Python : 3.12 (venv dans `.venv/`)
- Activer : `source .venv/bin/activate` ou `pylearn` (alias)
- Ajouter un package : `uv add <pkg>`
- Lancer les tests : `uv run pytest`

## Structure
- Scripts Python thématiques à la racine (decorators, generators, etc.)
- `utility/` : module partagé (`metrics.py`)
- `break-the-ice/` : exercices https://github.com/darkprinx/break-the-ice-with-python
- `regular-expressions/`, `unittest/`, etc. : exercices par thème

## Contexte
Apprentissage Python avancé. Exercices pratiques, pas de prod.
Ne pas installer de packages ML ici → utiliser l'env `ml` (conda).
