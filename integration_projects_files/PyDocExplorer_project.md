# PyDocExplorer — Extracteur de documentation de modules Python

> Projet d'intégration Python — Orienté Objet, Algorithmique, SQL, Interface Web
> Auteur : C.A.D. BONDJE DOUE
> Date : 2026-04-10
> Version : 1.0.0

---

## Table des matières

1. [Présentation du projet](#1-présentation-du-projet)
2. [Objectifs pédagogiques](#2-objectifs-pédagogiques)
3. [Architecture du projet](#3-architecture-du-projet)
4. [Modèle de données](#4-modèle-de-données)
5. [Description des modules](#5-description-des-modules)
6. [Schéma de la base de données SQLite](#6-schéma-de-la-base-de-données-sqlite)
7. [Interface web](#7-interface-web)
8. [Algorithmes clés](#8-algorithmes-clés)
9. [Feuille de route](#9-feuille-de-route)
10. [Dépendances](#10-dépendances)
11. [Lancement rapide](#11-lancement-rapide)

---

## 1. Présentation du projet

**PyDocExplorer** est une application web légère, écrite entièrement en Python, qui permet de :

- Charger dynamiquement un module Python (stdlib ou local)
- Extraire automatiquement sa documentation (docstrings, signatures, types, classes, méthodes)
- Stocker les données extraites dans une base **SQLite**
- Les afficher dans une **interface web navigable** servie par Python

L'application ne nécessite aucun framework externe lourd. Elle s'appuie sur les modules standards `inspect`, `ast`, `importlib`, `http.server`, et `sqlite3`.

---

## 2. Objectifs pédagogiques

| Critère                  | Couverture dans le projet                                      |
|--------------------------|----------------------------------------------------------------|
| **POO**                  | Classes `Module`, `DocClass`, `DocFunction`, `Param`           |
| **Algorithmique**        | Parcours récursif AST, tri, recherche full-text, scoring       |
| **SQL**                  | SQLite — CRUD, relations FK, requêtes filtrées                 |
| **Structuration du code**| Séparation extraction / stockage / rendu / serveur             |
| **Gestion des données**  | Sérialisation JSON, cache, mise à jour incrémentale            |
| **Documentation**        | Docstrings sur toutes les classes et méthodes du projet        |
| **Wiki web**             | Interface HTML servie en Python, navigation par module/classe  |

---

## 3. Architecture du projet

```
PyDocExplorer/
+-- app/
|   +-- __init__.py          # Init du package principal
|   +-- extractor.py         # Extraction via inspect + ast
|   +-- models.py            # Classes OO : Module, DocClass, DocFunction, Param
|   +-- database.py          # Couche SQLite (CRUD)
|   +-- server.py            # Serveur HTTP (http.server)
|   +-- renderer.py          # Generation HTML dynamique
|   +-- scorer.py            # Algorithme de score de qualite doc
+-- templates/
|   +-- index.html           # Liste des modules analyses
|   +-- module.html          # Detail d un module
|   +-- class.html           # Detail d une classe
|   +-- search.html          # Page de recherche full-text
+-- docs_cache/              # Cache JSON des modules analyses
+-- tests/
|   +-- test_extractor.py
|   +-- test_database.py
+-- main.py                  # Point d entree
+-- schema.sql               # DDL de la base SQLite
+-- requirements.txt         # Dependances (stdlib only)
+-- README.md
```

---

## 4. Modèle de données

### Classes Python (models.py)

```python
class Param:
    """Représente un paramètre de fonction."""
    name: str
    annotation: str | None
    default: str | None

class DocFunction:
    """Représente une fonction ou méthode documentée."""
    name: str
    docstring: str | None
    params: list[Param]
    return_type: str | None
    is_method: bool

class DocClass:
    """Représente une classe documentée."""
    name: str
    docstring: str | None
    methods: list[DocFunction]
    bases: list[str]

class DocModule:
    """Représente un module Python documenté."""
    name: str
    docstring: str | None
    classes: list[DocClass]
    functions: list[DocFunction]
    version: str | None
    file_path: str | None
    analyzed_at: str          # ISO datetime
```

### Héritage

```
DocBase  (nom, docstring, score)
  +-- DocFunction
  +-- DocClass
        +-- methodes: list[DocFunction]
  +-- DocModule
        +-- classes: list[DocClass]
        +-- functions: list[DocFunction]
```

---

## 6. Schéma de la base de données SQLite

```sql
-- schema.sql

CREATE TABLE IF NOT EXISTS modules (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,
    docstring   TEXT,
    version     TEXT,
    file_path   TEXT,
    doc_score   REAL    DEFAULT 0,
    analyzed_at TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS classes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id   INTEGER NOT NULL REFERENCES modules(id) ON DELETE CASCADE,
    name        TEXT    NOT NULL,
    docstring   TEXT,
    bases       TEXT,   -- JSON array
    doc_score   REAL    DEFAULT 0
);

CREATE TABLE IF NOT EXISTS functions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id   INTEGER REFERENCES modules(id) ON DELETE CASCADE,
    class_id    INTEGER REFERENCES classes(id) ON DELETE CASCADE,
    name        TEXT    NOT NULL,
    docstring   TEXT,
    return_type TEXT,
    is_method   INTEGER DEFAULT 0,
    doc_score   REAL    DEFAULT 0
);

CREATE TABLE IF NOT EXISTS params (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    function_id  INTEGER NOT NULL REFERENCES functions(id) ON DELETE CASCADE,
    name         TEXT    NOT NULL,
    annotation   TEXT,
    default_val  TEXT,
    position     INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_functions_module ON functions(module_id);
CREATE INDEX IF NOT EXISTS idx_functions_class  ON functions(class_id);
CREATE INDEX IF NOT EXISTS idx_classes_module   ON classes(module_id);
```

---

## 5. Description des modules

### `extractor.py` — Cœur algorithmique

Responsable de l'analyse d'un module Python via deux approches complémentaires :

- **`inspect`** : introspection à l'exécution (signatures, valeurs par défaut, docstrings)
- **`ast`** : analyse statique (annotations, constantes `__all__`, `__version__`)

```python
def extract_module(module_name: str) -> DocModule:
    """
    Charge et analyse un module Python.

    Args:
        module_name: Nom du module à analyser (ex: 'os', 'json')

    Returns:
        DocModule: Objet contenant toute la documentation extraite

    Raises:
        ImportError: Si le module ne peut pas être chargé
    """
    ...
```

---

### `database.py` — Couche d'accès aux données

Fournit une interface CRUD simple autour de SQLite.

Méthodes principales :

| Méthode                         | Description                             |
|---------------------------------|-----------------------------------------|
| `save_module(doc: DocModule)`   | Insère ou met à jour un module          |
| `get_module(name: str)`         | Récupère un module par son nom          |
| `list_modules()`                | Liste tous les modules analysés         |
| `search(query: str)`            | Recherche full-text sur docstrings      |
| `delete_module(name: str)`      | Supprime un module et ses données       |

---

### `scorer.py` — Algorithme de qualité

Calcule un **score de documentation** (0.0 -> 1.0) pour chaque entité :

```
score = (
    0.40 * has_docstring
  + 0.25 * ratio_params_typés
  + 0.20 * has_return_type
  + 0.10 * has_version         (modules seulement)
  + 0.05 * has_all             (modules seulement)
)
```

---

### `server.py` — Serveur HTTP

Serveur minimal basé sur `http.server.BaseHTTPRequestHandler`.

Routes :

| Route                  | Description                                 |
|------------------------|---------------------------------------------|
| `GET /`                | Page d'accueil — liste des modules          |
| `GET /module/<name>`   | Détail d'un module                          |
| `GET /class/<id>`      | Détail d'une classe                         |
| `GET /search?q=<term>` | Résultats de recherche full-text            |
| `POST /analyze`        | Soumettre un module à analyser              |

---

### `renderer.py` — Génération HTML

Transforme les objets Python en HTML à partir de templates simples (string.Template ou mini-moteur maison).

---

## 7. Interface web

L'interface présente :

- Un **formulaire de saisie** pour entrer le nom d'un module à analyser
- Une **barre de recherche** full-text
- La **liste des modules** avec leur score de documentation
- Une vue **module** : docstring, liste des classes et fonctions
- Une vue **classe** : héritage, méthodes, docstrings
- Un badge coloré pour le **score qualité** (rouge/orange/vert)

---

## 8. Algorithmes clés

### Parcours récursif AST

```
ast.parse(source_code)
  |
  +-- ast.walk(tree)
        |
        +-- isinstance(node, ast.ClassDef)  -> extraire classe
        +-- isinstance(node, ast.FunctionDef) -> extraire fonction
        +-- isinstance(node, ast.Assign)    -> chercher __version__, __all__
```

### Recherche full-text SQLite

```sql
SELECT m.name, f.name, f.docstring
FROM functions f
JOIN modules m ON f.module_id = m.id
WHERE f.docstring LIKE '%' || :query || '%'
UNION
SELECT m.name, c.name, c.docstring
FROM classes c
JOIN modules m ON c.module_id = m.id
WHERE c.docstring LIKE '%' || :query || '%'
ORDER BY 1, 2;
```

---

## 9. Feuille de route

### Phase 1 — Core (semaine 1-2)

- [x] Définition des modèles OO
- [x] Schéma SQL
- [ ] Extracteur `inspect` de base
- [ ] Couche CRUD SQLite
- [ ] Serveur HTTP minimal

### Phase 2 — Fonctionnalités (semaine 3)

- [ ] Parsing AST pour annotations et constantes
- [ ] Algorithme de scoring
- [ ] Cache JSON (docs_cache/)
- [ ] Interface web complète

### Phase 3 — Qualité (semaine 4)

- [ ] Tests unitaires (extractor, database)
- [ ] Export Markdown du wiki
- [ ] Mise à jour incrémentale (re-analyse sans recréer)
- [ ] Documentation du projet lui-même (docstrings complètes)

---

## 10. Dépendances

Uniquement la **bibliothèque standard Python 3.10+** :

| Module       | Usage                              |
|--------------|------------------------------------|
| `inspect`    | Introspection à l'exécution        |
| `ast`        | Analyse statique du code source    |
| `importlib`  | Chargement dynamique de modules    |
| `sqlite3`    | Base de données embarquée          |
| `http.server`| Serveur web minimal                |
| `json`       | Sérialisation du cache             |
| `pathlib`    | Gestion des chemins                |
| `datetime`   | Horodatage des analyses            |
| `unittest`   | Tests unitaires                    |

> Aucune dépendance externe requise (pas de Flask, pas de SQLAlchemy).

---

## 11. Lancement rapide

```bash
# Cloner ou créer le projet
mkdir PyDocExplorer && cd PyDocExplorer

# Initialiser la base de données
python main.py --init-db

# Lancer le serveur
python main.py --serve --port 8080

# Analyser un module depuis la ligne de commande
python main.py --analyze json
python main.py --analyze os.path

# Ouvrir dans le navigateur
# http://localhost:8080
```

---

*Document généré le 2026-04-10 — PyDocExplorer v1.0.0*
