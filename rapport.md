# Compte Rendu TP — Réponses aux Questions

## Question 1 : Différence entre `git init`, `git add` et `git commit`

* **`git init`** : Crée et initialise un nouveau dépôt Git local dans le dossier courant (création du dossier `.git`).
* **`git add`** : Ajoute les modifications du répertoire de travail à la zone d'indexation (*staging area*) en vue du prochain commit.
* **`git commit`** : Enregistre définitivement l'état des fichiers indexés dans l'historique du dépôt avec un message explicatif.

---

## Question 2 : Les dépôts distants et Git Push

### 1. Dépôt local vs Dépôt distant
* **Dépôt local** : Stocké sur votre ordinateur. Accessible sans connexion internet, utilisable uniquement par vous.
* **Dépôt distant** : Hébergé sur un serveur réseau/cloud (ex: GitHub). Permet de sauvegarder le code, partager avec une équipe et déclencher la CI/CD.

### 2. Le nom `origin`
`origin` est le nom par défaut donné à l'URL du dépôt distant. C'est un alias pour éviter de resaisir l'adresse HTTPS complète à chaque commande.

### 3. Rôle de `git push`
`git push` envoie vos commits locaux vers le dépôt distant sur GitHub pour mettre à jour la branche distante et déclencher les workflows d'intégration continue.

### 4. Utilité de l'option `-u` (`--set-upstream`)
L'option `-u` associe la branche locale à la branche distante correspondante. Une fois configurée, il suffit d'utiliser les commandes courtes `git push` ou `git pull` sans préciser `origin main`.

---

## Question 3 : Environnement virtuel et test d'exception

### 1. Intérêt d'un environnement virtuel Python (`.venv`)
Un environnement virtuel isole le projet du système global. Il permet d'installer les packages et leurs versions spécifiques (ex: `pytest`) uniquement pour ce projet, sans polluer l'installation globale de Python ni provoquer de conflits entre les dépendances de différents projets.

### 2. Pourquoi le test de division par zéro réussit-il alors qu'une exception est levée ?
Le test utilise le contexte `pytest.raises(ZeroDivisionError)`. Ce bloc **intercepte intentionnellement** l'exception attendue. Le test valide que le programme se comporte correctement en levant cette erreur spécifique. Si le programme ne levait *pas* d'exception ou levait un autre type d'erreur, le test échouerait.

---

## Question 4 : Déclenchement automatique de la CI

Le premier push sur `main` déclenche le workflow sans Pull Request car le fichier `.github/workflows/ci-cd.yml` contient l'événement de déclenchement direct sur les commits poussés sur cette branche :

```yaml
on:
  push:
    branches: [main]
```

Ainsi, l'événement `push` s'exécute immédiatement lors du transfert de la branche vers GitHub.

---

## Question 5 : Diagnostic de régression dans la CI

### 1. Pourquoi le test détecte-t-il la régression ?
Dans `tests/test_calculator.py` (ligne 7), l'instruction `assert add(2, 3) == 5` vérifie que le résultat de l'appel est égal à `5`. Comme la fonction `add` a été remplacée par une soustraction, `add(2, 3)` renvoie `-1`. L'assertion échoue (`AssertionError : assert -1 == 5`), ce qui fait échouer le test (`FAILED`) et renvoie le code de sortie `1`.

### Le test se nomme <-pyhton->

### 2. Que vous apprend le journal que l'icône rouge ne montre pas ?
L'icône rouge sur la Pull Request #1 (`test/regression-add`) signale uniquement que la vérification globale a échoué. Le journal détaillé fournit le diagnostic exact :
* **Le bilan des tests :** 1 test en échec (`FAILED`) et 5 tests réussis (`PASSED`).
* **Le nom exact du test fautif :** `tests/test_calculator.py::test_add` (à la ligne 7).
* **La comparaison des valeurs :** la valeur attendue (`5`) face à la valeur réellement obtenue (`-1`).
* **L'étape bloquante et le code d'erreur :** l'arrêt s'est produit à l'étape `Run python -m pytest -v` avec un code de sortie non nul (`exit code 1`).