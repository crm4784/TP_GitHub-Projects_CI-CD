# Projet support — calculatrice Python

Projet Python utilisé dans le TP CI. Il contient des fonctions de calcul, six tests `pytest` et un workflow GitHub Actions. Le workflow vérifie automatiquement le code ; il ne construit ni ne déploie une application.

## Lancer les tests en local

À la racine du dépôt, créez et activez un environnement virtuel.

**Linux/macOS :**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

**Windows PowerShell :**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v
```

Résultat attendu : `6 passed`. Le dossier `.venv` et les fichiers de cache sont exclus du dépôt par `.gitignore`.

## CI GitHub Actions

Le workflow `.github/workflows/ci-cd.yml` s’exécute sur les push vers `main` et les pull requests qui ciblent `main`. Il installe Python 3.11 et pytest, puis exécute `python -m pytest -v`. L’onglet **Actions** du dépôt permet de consulter les étapes et leurs journaux.
