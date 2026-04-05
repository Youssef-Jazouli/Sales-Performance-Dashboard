import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Superstore Dashboard", layout="wide")
st.title("Tableau de Bord - Performance Superstore")
st.markdown("---")

@st.cache_resource
def init_connection():
    db_url = "postgresql://postgres:1919@localhost:5432/superstore_db"
    return create_engine(db_url)

engine = init_connection()

@st.cache_data
def load_data():
    df_orders = pd.read_sql("SELECT * FROM orders", engine)
    df_customers = pd.read_sql("SELECT * FROM customers", engine)
    df_products = pd.read_sql("SELECT * FROM products", engine)
    df_geography = pd.read_sql("SELECT * FROM geography", engine)
    
    df = pd.merge(df_orders, df_customers, on="Customer ID")
    df = pd.merge(df, df_products, on="Product ID")
    df = pd.merge(df, df_geography, on="geo_id")
    
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Année'] = df['Order Date'].dt.year
    return df

try:
    df = load_data()
    
    st.sidebar.header("Filtres Interactifs")
    annee_filter = st.sidebar.multiselect("Période (Année)", df['Année'].unique(), default=df['Année'].unique())
    region_filter = st.sidebar.multiselect("Région", df['Region'].unique(), default=df['Region'].unique())
    category_filter = st.sidebar.multiselect("Catégorie", df['Category'].unique(), default=df['Category'].unique())
    
    df_filtered = df[(df['Année'].isin(annee_filter)) & (df['Region'].isin(region_filter)) & (df['Category'].isin(category_filter))]
    
    col1, col2, col3, col4 = st.columns(4)
    total_sales = df_filtered['Sales'].sum()
    total_profit = df_filtered['profit'].sum()
    margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0
    
    col1.metric("Ventes Totales", f"{total_sales:,.0f} $")
    col2.metric("Profit Total", f"{total_profit:,.0f} $")
    col3.metric("Marge Bénéficiaire", f"{margin:.1f} %")
    col4.metric("Total Commandes", f"{len(df_filtered):,}")
    
    st.markdown("---")

    st.subheader("1. Statistiques Descriptives (Tableau)")
    stats_df = df_filtered[['Sales', 'profit']].describe().T
    st.dataframe(stats_df.style.format("{:.2f}"))
    
    st.markdown("---")
    
    st.subheader("2. Visualisations (4 Graphiques)")
    
    fig_col1, fig_col2 = st.columns(2)
    
    with fig_col1:
        st.markdown("**Répartition par Région (Secteurs)**")
        sales_reg = df_filtered.groupby('Region')['Sales'].sum()
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.pie(sales_reg, labels=sales_reg.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
        ax1.axis('equal') 
        fig1.patch.set_alpha(0.0)
        st.pyplot(fig1)
        
    with fig_col2:
        st.markdown("**Tendance des Ventes (Lignes)**")
        df_trend = df_filtered.groupby('Order Date')['Sales'].sum()
        st.line_chart(df_trend)

    fig_col3, fig_col4 = st.columns(2)

    with fig_col3:
        st.markdown("**Top 10 Produits (Barres)**")
        top_products = df_filtered.groupby('Product Name')['profit'].sum().sort_values(ascending=False).head(10)
        st.bar_chart(top_products)

    with fig_col4:
        st.markdown("**Ventes vs Profit par Catégorie (Seaborn)**")
        fig4, ax4 = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=df_filtered, x='Sales', y='profit', hue='Category', alpha=0.6, ax=ax4)
        fig4.patch.set_alpha(0.0)
        ax4.set_facecolor("none")
        st.pyplot(fig4)

except Exception as e:
    st.error(f"Erreur : {e}")
