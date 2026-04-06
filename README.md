# 📊 Superstore Sales Dashboard

An interactive sales performance dashboard built with **Streamlit**, **PostgreSQL**, and **Matplotlib/Seaborn**.

## 📋 Overview

This app connects to a PostgreSQL database, merges data from multiple tables, and renders an interactive dashboard with KPI metrics, filters, descriptive statistics, and 4 visualizations — all in a wide-layout Streamlit interface.

## 📁 Files

| File | Description |
|------|-------------|
| `store_sales_dashboard.py` | Main Streamlit application |

## 🗄️ Database

The app connects to a **PostgreSQL** database named `superstore_db` and reads from 4 tables:

| Table | Key Column |
|-------|-----------|
| `orders` | `Customer ID`, `Product ID`, `Order Date`, `Sales`, `profit` |
| `customers` | `Customer ID` |
| `products` | `Product ID`, `Product Name`, `Category` |
| `geography` | `geo_id`, `Region` |

> **Default connection:** `postgresql://postgres:1919@localhost:5432/superstore_db`  
> Update the `db_url` in `init_connection()` to match your environment.

## 🔧 Requirements

```bash
pip install streamlit pandas sqlalchemy psycopg2-binary matplotlib seaborn
```

## 🚀 Usage

```bash
streamlit run store_sales_dashboard.py
```

Then open `http://localhost:8501` in your browser.

## 🎛️ Sidebar Filters

| Filter | Description |
|--------|-------------|
| **Période (Année)** | Filter by one or more order years |
| **Région** | Filter by one or more regions |
| **Catégorie** | Filter by product category |

All filters are multi-select and default to showing all values.

## 📈 Dashboard Sections

### KPI Metrics (Top Row)
| Metric | Description |
|--------|-------------|
| Ventes Totales | Total sales revenue |
| Profit Total | Total profit |
| Marge Bénéficiaire | Profit margin (%) |
| Total Commandes | Number of orders |

### 1. Descriptive Statistics
A summary table (`describe()`) for `Sales` and `profit` columns, transposed for readability.

### 2. Visualizations

| Chart | Type | Description |
|-------|------|-------------|
| Répartition par Région | Pie chart | Sales share per region |
| Tendance des Ventes | Line chart | Daily sales trend over time |
| Top 10 Produits | Bar chart | Top 10 products by profit |
| Ventes vs Profit | Scatter plot | Sales vs. profit colored by category |

## ⚙️ Architecture

```
PostgreSQL DB
  ├── orders
  ├── customers
  ├── products
  └── geography
        │
        ▼
   Merged DataFrame  ──▶  Sidebar Filters  ──▶  KPIs + Charts
```

Data loading and DB connection are both cached (`@st.cache_data` / `@st.cache_resource`) for performance.

## ⚠️ Error Handling

Any database connection or query error is caught and displayed inline via `st.error()`.
