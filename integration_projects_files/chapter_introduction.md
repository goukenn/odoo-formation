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
6. [Schéma de la base de données PostgreSQL](#6-schéma-de-la-base-de-données-postgresql)

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
- Stocker les données extraites dans une base **PostgreSQL** (localhost)
- Les afficher dans une **interface web navigable** servie par Python

L'application s'appuie sur les modules standards `inspect`, `ast`, `importlib`, `http.server`, ainsi que sur le driver **psycopg** (psycopg3) pour la communication avec PostgreSQL.

---

## 2. Objectifs pédagogiques

| Critère                  | Couverture dans le projet                                      |
|--------------------------|----------------------------------------------------------------|
| **POO**                  | Classes `Module`, `DocClass`, `DocFunction`, `Param`           |
| **Algorithmique**        | Parcours récursif AST, tri, recherche full-text, scoring       |
| **SQL**                  | PostgreSQL — CRUD, relations FK, requêtes filtrées, ILIKE      |
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
|   +-- database.py          # Couche PostgreSQL/psycopg3 (CRUD)
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
+-- schema.sql               # DDL PostgreSQL
+-- requirements.txt         # psycopg[binary], etc.
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

## 6. Schéma de la base de données PostgreSQL

> Driver : **psycopg3** (`psycopg[binary]`) — connexion localhost
> Stratégie de connexion : déterminée par le projet (pool ou connexion directe selon la charge)

### Configuration de connexion (`config.py`)

```python
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "dbname":   "pydocexplorer",
    "user":     "pydoc_user",
    "password": "changeme",
}

# Connection string psycopg3
DSN = "postgresql://{user}:{password}@{host}:{port}/{dbname}".format(**DB_CONFIG)
```

### DDL — `schema.sql`

```sql
-- schema.sql — PostgreSQL

CREATE TABLE IF NOT EXISTS modules (
    id          SERIAL          PRIMARY KEY,
    name        VARCHAR(255)    NOT NULL UNIQUE,
    docstring   TEXT,
    version     VARCHAR(50),
    file_path   TEXT,
    doc_score   NUMERIC(4,3)    DEFAULT 0,
    analyzed_at TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS classes (
    id          SERIAL          PRIMARY KEY,
    module_id   INTEGER         NOT NULL REFERENCES modules(id) ON DELETE CASCADE,
    name        VARCHAR(255)    NOT NULL,
    docstring   TEXT,
    bases       JSONB,          -- tableau JSON des classes parentes
    doc_score   NUMERIC(4,3)    DEFAULT 0
);

CREATE TABLE IF NOT EXISTS functions (
    id          SERIAL          PRIMARY KEY,
    module_id   INTEGER         REFERENCES modules(id) ON DELETE CASCADE,
    class_id    INTEGER         REFERENCES classes(id) ON DELETE CASCADE,
    name        VARCHAR(255)    NOT NULL,
    docstring   TEXT,
    return_type VARCHAR(255),
    is_method   BOOLEAN         DEFAULT FALSE,
    doc_score   NUMERIC(4,3)    DEFAULT 0
);

CREATE TABLE IF NOT EXISTS params (
    id           SERIAL          PRIMARY KEY,
    function_id  INTEGER         NOT NULL REFERENCES functions(id) ON DELETE CASCADE,
    name         VARCHAR(255)    NOT NULL,
    annotation   VARCHAR(255),
    default_val  TEXT,
    position     SMALLINT        NOT NULL
);

-- Index
CREATE INDEX IF NOT EXISTS idx_functions_module ON functions(module_id);
CREATE INDEX IF NOT EXISTS idx_functions_class  ON functions(class_id);
CREATE INDEX IF NOT EXISTS idx_classes_module   ON classes(module_id);

-- Index full-text natif PostgreSQL
CREATE INDEX IF NOT EXISTS idx_functions_doc_fts
    ON functions USING GIN (to_tsvector('english', COALESCE(docstring, '')));
CREATE INDEX IF NOT EXISTS idx_classes_doc_fts
    ON classes USING GIN (to_tsvector('english', COALESCE(docstring, '')));
```

### Différences notables vs SQLite

| Aspect            | SQLite (ancienne version)    | PostgreSQL (actuel)                     |
|-------------------|------------------------------|-----------------------------------------|
| Clé primaire      | `INTEGER AUTOINCREMENT`      | `SERIAL`                                |
| Booléen           | `INTEGER 0/1`                | `BOOLEAN TRUE/FALSE`                    |
| JSON              | `TEXT`                       | `JSONB` (indexable, requêtable)         |
| Full-text search  | `LIKE '%...%'`               | `tsvector` + `GIN` (performant)         |
| Horodatage        | `TEXT` ISO                   | `TIMESTAMPTZ` (timezone-aware)          |
| Précision décimal | `REAL`                       | `NUMERIC(4,3)` (exact)                  |

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

Fournit une interface CRUD construite autour de **psycopg3** (`psycopg[binary]`).
La stratégie de connexion (directe ou pool) est encapsulée dans une classe `Database`
qui expose un context manager, laissant le projet décider du mode selon la charge.

```python
class Database:
    """Gestionnaire de connexion PostgreSQL via psycopg3."""

    def __init__(self, dsn: str) -> None: ...
    def __enter__(self) -> "Database": ...
    def __exit__(self, *args) -> None: ...
```

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

### Recherche full-text PostgreSQL (tsvector + GIN)

```sql
-- Recherche full-text native PostgreSQL
SELECT m.name, f.name, f.docstring
FROM functions f
JOIN modules m ON f.module_id = m.id
WHERE to_tsvector('english', COALESCE(f.docstring, ''))
      @@ plainto_tsquery('english', %(query)s)

UNION

SELECT m.name, c.name, c.docstring
FROM classes c
JOIN modules m ON c.module_id = m.id
WHERE to_tsvector('english', COALESCE(c.docstring, ''))
      @@ plainto_tsquery('english', %(query)s)

ORDER BY 1, 2;
```

> `plainto_tsquery` est utilisé à la place de `to_tsquery` pour accepter
> des termes de recherche libres sans syntaxe spéciale.

---

## 9. Feuille de route

### Phase 1 — Core (semaine 1-2)

- [x] Définition des modèles OO
- [x] Schéma SQL
- [ ] Extracteur `inspect` de base
- [ ] Couche CRUD PostgreSQL (psycopg3)
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

### Bibliothèque standard Python 3.10+

| Module        | Usage                              |
|---------------|------------------------------------|
| `inspect`     | Introspection à l'exécution        |
| `ast`         | Analyse statique du code source    |
| `importlib`   | Chargement dynamique de modules    |
| `http.server` | Serveur web minimal                |
| `json`        | Sérialisation du cache             |
| `pathlib`     | Gestion des chemins                |
| `datetime`    | Horodatage des analyses            |
| `unittest`    | Tests unitaires                    |

### Dépendance externe

| Package            | Usage                                        |
|--------------------|----------------------------------------------|
| `psycopg[binary]`  | Driver PostgreSQL natif (psycopg3)           |

```
# requirements.txt
psycopg[binary]>=3.1
```

> PostgreSQL doit être installé et accessible sur `localhost:5432`.

---

## 11. Lancement rapide

```bash
# Cloner ou créer le projet
mkdir PyDocExplorer && cd PyDocExplorer

# Installer les dépendances
pip install psycopg[binary]

# Créer la base PostgreSQL (une seule fois)
createdb pydocexplorer
psql pydocexplorer < schema.sql

# Initialiser la configuration
cp config.example.py config.py
# -> éditer config.py avec vos identifiants PostgreSQL

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