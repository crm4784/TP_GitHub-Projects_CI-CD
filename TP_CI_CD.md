# TP — Découvrir l’intégration continue avec GitHub Actions

**Python · Git · GitHub · pytest**

## Objectifs

Travailler sur une branche, exécuter des tests Python et lire le résultat d’une intégration continue (CI) sur une pull request.

Une **CI** relance automatiquement des vérifications quand du code est envoyé sur GitHub. Dans ce TP, ces vérifications sont des tests `pytest`. Une CI verte indique que les contrôles prévus ont réussi ; elle ne prouve pas qu’un programme est sans défaut.

**Prérequis :** Python 3.11 ou plus récent, Git, un éditeur, un compte GitHub et l’accès à un dépôt de travail. Toutes les commandes Git ci-dessous sont lancées à la racine du dépôt.

## 1. Créer votre projet en local

Dans un premier temps, vous allez construire votre projet directement sur votre ordinateur, sans passer par GitHub.

### 1.1 Créer le dossier du projet

Créez un dossier nommé :

text

```text
TP_GitHub-Projects_CI-CD
```

Ouvrez ce dossier dans votre éditeur de code (Visual Studio Code).

### 1.2 Créer l'arborescence

À partir de l'arborescence fournie dans l'énoncé, créez les dossiers et les fichiers nécessaires.

```text
TP_GitHub-Projects_CI-CD/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── app/
│   ├── __init__.py
│   └── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

Attention : le dossier `.github/workflows` doit être créé manuellement. Il contiendra le fichier de configuration de GitHub Actions.

### 1.3 Initialiser Git

Ouvrez un terminal à la racine du dossier du projet.

Vérifiez que vous êtes dans le bon répertoire :

```bash
pwd
```

Initialisez ensuite votre dépôt Git :

```bash
git init
```

Configurez la branche principale avec le nom `main` :

```bash
git branch -M main
```

Vérifiez l'état du dépôt :

```bash
git status
git branch --show-current
```

**Résultat attendu :** vous disposez maintenant d'un dépôt Git local, positionné sur la branche `main`.

### 1.4 Effectuer le premier commit

Ajoutez les fichiers du projet à l'index Git :

```bash
git add .
```

Vérifiez les fichiers qui seront enregistrés :

```bash
git status
```

Effectuez votre premier commit :

```bash
git commit -m "Initialisation du projet"
```

Vérifiez l'historique :

```bash
git log --oneline
```

**Résultat attendu :** votre premier commit apparaît dans l'historique Git.

**Question 1.** Quelle est la différence entre `git init`, `git add` et `git commit` ?

## 2. Publier votre dépôt sur GitHub

Votre projet existe maintenant uniquement sur votre ordinateur.

Vous allez créer un dépôt distant sur GitHub afin d'y envoyer votre travail.

### 2.1 Créer un nouveau dépôt GitHub

1. Connectez-vous à votre compte GitHub.
2. Cliquez sur **New repository**.
3. Donnez au dépôt le nom :

```text
TP_GitHub-Projects_CI-CD
```

4. Ajoutez éventuellement une description : `TP BTS CIEL - Découverte de GitHub Actions`.
5. Choisissez un dépôt public.
6. Ne cochez aucune des options suivantes :
   - Add a README file ;
   - Add .gitignore ;
   - Choose a license.
7. Cliquez sur **Create repository**.

**Important :** le dépôt GitHub doit être vide, car vous avez déjà créé et initialisé votre projet en local.

### 2.2 Relier votre dépôt local à GitHub

GitHub vous propose une URL HTTPS pour votre nouveau dépôt.

Dans votre terminal, toujours à la racine de votre projet, exécutez :

```bash
git remote add origin https://github.com/VOTRE_COMPTE/TP_GitHub-Projects_CI-CD.git
```

Remplacez `VOTRE_COMPTE` par votre identifiant GitHub.

Vérifiez la configuration :

```bash
git remote -v
```

Vous devez voir apparaître votre dépôt GitHub comme dépôt distant nommé `origin`.

### 2.3 Envoyer votre projet sur GitHub

Envoyez votre branche principale sur GitHub :

```bash
git push -u origin main
```

Git peut vous demander de vous authentifier auprès de GitHub.

Après le push, actualisez la page de votre dépôt GitHub.

**Résultat attendu :** vous devez retrouver sur GitHub l'ensemble des fichiers et dossiers créés localement.

### 2.4 Vérifier la synchronisation

Exécutez les commandes suivantes :

```bash
git status
git branch -vv
git remote -v
```

**Question 2.**

1. Quelle est la différence entre un dépôt local et un dépôt distant ?
2. À quoi correspond le nom `origin` ?
3. Quel est le rôle de la commande `git push` ?
4. À quoi sert l'option `-u` dans `git push -u origin main` ?

### 2.5 Installer le projet et lancer ses tests

Le projet contient le module `app/calculator.py`, ses tests dans `tests/test_calculator.py` et la dépendance `pytest` dans `requirements.txt`. Un **environnement virtuel** isole les outils Python du projet.

**Linux ou macOS :**

```bash
python3 -m venv .venv
source .venv/bin/activate
python --version
python -m pip install -r requirements.txt
python -m pytest -v
```

**Windows PowerShell :**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
python -m pip install -r requirements.txt
python -m pytest -v
```

Si l’activation est bloquée dans PowerShell, utilisez directement `\.venv\Scripts\python.exe -m pip install -r requirements.txt` puis `\.venv\Scripts\python.exe -m pytest -v`.

Résultat attendu : six tests passent. `python -m pytest` lance pytest avec l’interpréteur Python actif. Dans chaque test, `assert` compare le résultat obtenu à celui attendu. `pytest.raises` vérifie qu’une exception précise est levée.

**Questions 3.** Quel est l’intérêt d’un environnement virtuel ? Pourquoi le test de division par zéro peut-il réussir alors que le programme lève une exception ?

## 3. Comprendre la structure et ignorer les fichiers locaux

Repérez ces fichiers et dossiers :

```text
.github/workflows/ci-cd.yml   configuration de la CI
app/calculator.py             fonctions testées
tests/test_calculator.py      vérifications automatiques
requirements.txt              dépendances Python
.gitignore                    fichiers à ne pas versionner
```

Le dossier `.venv` et les caches ne doivent pas être envoyés sur GitHub. Vérifiez que `.gitignore` contient au minimum :

```gitignore
.venv/
venv/
__pycache__/
*.py[cod]
.pytest_cache/
.env
```

`.gitignore` empêche Git de proposer ces fichiers non suivis. Il ne retire pas du dépôt un fichier déjà versionné.

## 4. Lire le workflow

Ouvrez `.github/workflows/ci-cd.yml`. Le workflow fourni suit le modèle ci-dessous :

```yaml
name: CI Python

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

permissions:
  contents: read

jobs:
  tests:
    name: Tests Python
    runs-on: ubuntu-latest
    steps:
      - name: Récupérer le code
        uses: actions/checkout@v6

      - name: Installer Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.11"

      - name: Installer les dépendances
        run: python -m pip install -r requirements.txt

      - name: Exécuter les tests
        run: python -m pytest -v
```

Repères : `on` choisit les événements ; `jobs` décrit le travail ; `runs-on` choisit la machine ; `steps` sont exécutées dans l’ordre ; `uses` appelle une action réutilisable ; `run` lance une commande. `checkout` récupère le dépôt sur la machine de CI. `setup-python` installe la version choisie.

Ici, le workflow démarre après un push sur `main` ou une pull request dont la branche cible est `main`. Un push sur une branche sans pull request ne le déclenche pas. Chaque exécution repart d’une machine propre : elle installe les dépendances déclarées et ne réutilise pas votre `.venv`.

## 5. Observer la première CI (intégration continue) sur GitHub

```bash
git status
git remote -v
```

Lors de l'envoi de votre branche `main` sur GitHub avec la commande `git push -u origin main`, vous avez déclenché automatiquement le workflow GitHub Actions.

En effet, le fichier `.github/workflows/ci-cd.yml` contient le déclencheur suivant :

yaml

```yaml
on:
  push:
    branches: [main]
```

Dans ce workflow, un push sur `main` déclenche la CI car l’événement `push` est filtré sur la branche `main`. Cela est indépendant de l’existence d’une pull request.

### Observer le résultat

1. Ouvrez votre dépôt sur GitHub.
2. Cliquez sur l'onglet **Actions**.
3. Sélectionnez le workflow **CI Python**.
4. Ouvrez la première exécution.
5. Consultez le job **Tests Python** et ses différentes étapes.

**Résultat attendu :**

- Le workflow démarre automatiquement après le premier push.
- Les dépendances Python sont installées.
- Les tests pytest sont exécutés.
- Les six tests réussissent.
- Le workflow affiche une coche verte.

Ouvrez les journaux pour identifier les commandes réellement exécutées.

**Question 4.** Pourquoi le premier push sur `main` déclenche-t-il automatiquement la CI alors qu'aucune pull request n'a encore été créée ?

## 6. Provoquer une erreur et lire le diagnostic

Créez une branche de travail :

```bash
git switch main
git pull --ff-only
git switch -c test/regression-add
```

Dans `app/calculator.py`, remplacez temporairement l’addition par une soustraction :

```python
def add(a, b):
    return a - b
```

Relancez les tests :

```bash
python -m pytest -v
```

Résultat attendu : un test échoue et cinq réussissent. Notez le nom du test, la valeur attendue, la valeur obtenue et le code de sortie. Pour afficher ce code juste après pytest : `echo $?` sous Bash/Zsh ou `$LASTEXITCODE` sous PowerShell. Un code `0` indique normalement une commande réussie ; un code non nul signale un échec.

Envoyez cette version volontairement erronée sur votre branche :

```bash
git add app/calculator.py
git diff --cached
git diff --cached --check
git commit -m "Introduit une régression pour observer la CI"
git push -u origin test/regression-add
```

Le push sur cette branche seule ne lance pas le workflow, car le déclencheur `push` est limité à `main`. Sur GitHub, ouvrez **Pull requests → New pull request**. Choisissez `main` comme branche de destination (**base**) et `test/regression-add` comme branche source (**compare**). Créez la pull request avec un titre explicite.

La CI doit démarrer et échouer sur `test_add`. Dans **Checks**, ouvrez le contrôle en échec. Relevez le nom du test, les valeurs attendue et obtenue, et la première étape en rouge. Un résultat rouge signifie que le contrôle n’a pas réussi ; ne fusionnez pas cette pull request.

**Question 5.** Pourquoi le test détecte-t-il la régression ? Que vous apprend le journal que l’icône rouge ne montre pas ?

## 7. Corriger, pousser et relire

Dans `app/calculator.py`, remettez `return a + b`. Relancez `python -m pytest -v` : les six tests doivent réussir. Enregistrez aussi dans le `README.md` du projet une courte trace du diagnostic : cause de l’échec, correction et résultat après correction.

```bash
git add app/calculator.py README.md
git diff --cached
git commit -m "Corrige la fonction add"
git push
```

Le push met à jour la même pull request et déclenche une nouvelle CI. Vérifiez le nouveau résultat et le commit testé. Une pull request sert à proposer des changements, à les discuter et à voir les contrôles avant de les intégrer.

Lorsque la CI est verte et la relecture faite, fusionnez, puis mettez à jour votre branche locale :

```bash
git switch main
git pull --ff-only
git status
```

## 8. Bilan et compte rendu

Répondez aux questions du TP.

Joignez ou décrivez les éléments suivants :

- Le nom de votre dépôt GitHub et son URL.
- Le nom de la branche principale utilisée.
- Une capture d'écran de votre dépôt GitHub contenant l'arborescence du projet.
- Une capture ou le lien vers votre pull request avec le contrôle rouge puis le contrôle vert.
- Le nom du test en échec, la cause de la régression et la correction effectuée.
- Une phrase expliquant la différence entre un test exécuté localement et une CI exécutée par GitHub.

**Conclusion :** Git conserve l'historique des changements ; GitHub héberge le dépôt et facilite le travail par pull request ; pytest exécute les tests ; GitHub Actions automatise leur exécution.

## Annexe - Ordre des opérations

Respecter cet ordre de commandes :

Sur l'ordinateur :

```bash
mkdir TP_GitHub-Projects_CI-CD
cd TP_GitHub-Projects_CI-CD
git init
git branch -M main
```

Après création des fichiers :

```bash
git add .
git commit -m "Initialisation du projet"
```

Sur GitHub :

Création d'un dépôt distant vide.

Retour dans le terminal

```bash
git remote add origin URL_DU_DEPOT
git push -u origin main
```

Projet publié sur GitHub

---
