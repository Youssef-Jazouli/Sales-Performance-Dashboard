# 📊 Tableau de Bord - Performance Superstore

Application web interactive développée avec **Streamlit** pour analyser les performances commerciales d'un magasin Superstore à partir d'une base de données PostgreSQL.

---

## 🗂️ Structure du Projet

```
superstore-dashboard/
├── app.py                  # Application principale Streamlit
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation du projet
```

---

## ⚙️ Prérequis

- Python 3.8+
- PostgreSQL 12+
- Base de données `superstore_db` configurée et peuplée

---

## 🗄️ Schéma de la Base de Données

L'application s'attend à trouver les tables suivantes dans `superstore_db` :

| Table         | Colonnes clés                                      |
|---------------|----------------------------------------------------|
| `orders`      | `Order ID`, `Customer ID`, `Product ID`, `geo_id`, `Order Date`, `Sales`, `profit` |
| `customers`   | `Customer ID`, `Customer Name`, `Segment`          |
| `products`    | `Product ID`, `Product Name`, `Category`, `Sub-Category` |
| `geography`   | `geo_id`, `Region`, `State`, `City`                |

---

## 🚀 Installation & Lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/superstore-dashboard.git
cd superstore-dashboard
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

**`requirements.txt` :**
```
streamlit
pandas
sqlalchemy
psycopg2-binary
matplotlib
seaborn
```

### 4. Configurer la connexion PostgreSQL

Dans `app.py`, modifier la ligne suivante selon votre configuration :

```python
db_url = "postgresql://USER:PASSWORD@HOST:PORT/superstore_db"
```

| Paramètre  | Valeur par défaut |
|------------|-------------------|
| Utilisateur | `postgres`        |
| Mot de passe | `1919`           |
| Hôte       | `localhost`        |
| Port       | `5432`             |
| Base       | `superstore_db`    |

### 5. Lancer l'application

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : **http://localhost:8501**

---

## 🎛️ Fonctionnalités

### Filtres interactifs (barre latérale)

- **Période (Année)** — filtre multi-sélection par année de commande
- **Région** — filtre par région géographique
- **Catégorie** — filtre par catégorie de produit

### KPIs (indicateurs clés)

| Indicateur           | Description                              |
|----------------------|------------------------------------------|
| Ventes Totales       | Somme des ventes filtrées (en $)         |
| Profit Total         | Somme des profits filtrés (en $)         |
| Marge Bénéficiaire   | Ratio profit / ventes (en %)             |
| Total Commandes      | Nombre de lignes de commandes filtrées   |

### Statistiques descriptives

Tableau interactif affichant les métriques statistiques (`count`, `mean`, `std`, `min`, `max`, quartiles) pour les colonnes `Sales` et `profit`.

### Visualisations

| Graphique | Type | Description |
|-----------|------|-------------|
| Répartition par Région | Camembert (Matplotlib) | Part des ventes par région |
| Tendance des Ventes | Courbe (Streamlit) | Évolution des ventes dans le temps |
| Top 10 Produits | Barres (Streamlit) | Produits les plus profitables |
| Ventes vs Profit | Nuage de points (Seaborn) | Corrélation ventes/profit par catégorie |

---

## 🛠️ Technologies Utilisées

| Technologie   | Rôle                                  |
|---------------|---------------------------------------|
| Streamlit     | Interface web interactive             |
| Pandas        | Manipulation et analyse des données   |
| SQLAlchemy    | Connexion et requêtes PostgreSQL      |
| Matplotlib    | Graphiques personnalisés              |
| Seaborn       | Visualisations statistiques avancées  |
| PostgreSQL    | Base de données relationnelle         |

---

## 🐛 Gestion des Erreurs

L'application affiche un message d'erreur clair (`st.error`) en cas de problème de connexion à la base de données ou de données manquantes. Vérifiez dans ce cas :

1. Que le service PostgreSQL est bien démarré
2. Que les identifiants de connexion sont corrects
3. Que les 4 tables existent et contiennent des données

---

## 📌 Notes

- Les données sont mises en cache avec `@st.cache_data` pour des performances optimales.
- La connexion à la base de données est mise en cache avec `@st.cache_resource` pour éviter les reconnexions répétées.
