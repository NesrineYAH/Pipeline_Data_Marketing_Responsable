import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Numberly Marketing Analytics",
    page_icon="📊",
    layout="wide"
)

# Titre avec le branding Numberly
st.title(" Numberly - Dashboard Marketing Analytics")
st.markdown("**Simulation de données clients pour campagnes marketing responsables**")

# Chargement des données
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/donnees_marketing.csv')
        df['date'] = pd.to_datetime(df['date'])
        return df
    except FileNotFoundError:
        st.error("Fichier de données non trouvé. Veuillez d'abord exécuter l'ETL.")
        return None

df = load_data()

if df is not None:
    # ===== KPI PRINCIPAUX =====
    st.header("📈 KPIs Principaux")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_clients = df['client_id'].nunique()
        st.metric("Clients Uniques", f"{total_clients:,}")
    
    with col2:
        taux_conversion = df['est_achat'].mean() * 100
        st.metric("Taux de Conversion", f"{taux_conversion:.1f}%")
    
    with col3:
        ca_total = df['valeur_achat'].sum()
        st.metric("Chiffre d'Affaires", f"€{ca_total:,.0f}")
    
    with col4:
        panier_moyen = df[df['valeur_achat'] > 0]['valeur_achat'].mean()
        st.metric("Panier Moyen", f"€{panier_moyen:.0f}")

    # ===== PERFORMANCE PAR CANAL =====
    st.header("📊 Performance par Canal d'Acquisition")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Taux de conversion par canal
        conv_par_canal = df.groupby('canal_acquisition')['est_achat'].mean() * 100
        fig_conv = px.bar(
            conv_par_canal, 
            title="Taux de Conversion par Canal",
            labels={'value': 'Taux de Conversion (%)', 'canal_acquisition': 'Canal'}
        )
        st.plotly_chart(fig_conv, use_container_width=True)
    
    with col2:
        # Répartition des canaux
        repartition_canal = df['canal_acquisition'].value_counts()
        fig_repartition = px.pie(
            values=repartition_canal.values,
            names=repartition_canal.index,
            title="Répartition des Canaux d'Acquisition"
        )
        st.plotly_chart(fig_repartition, use_container_width=True)

    # ===== SEGMENTATION CLIENTS =====
    st.header("👥 Segmentation Clients")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Par segment
        segment_count = df['segment'].value_counts()
        fig_segment = px.pie(
            values=segment_count.values,
            names=segment_count.index,
            title="Répartition par Segment Client"
        )
        st.plotly_chart(fig_segment, use_container_width=True)
    
    with col2:
        # Par âge
        fig_age = px.histogram(
            df, 
            x='age', 
            title="Distribution des Âges",
            nbins=20
        )
        st.plotly_chart(fig_age, use_container_width=True)

    # ===== TENDANCE TEMPORELLE =====
    st.header("📅 Évolution Temporelle")
    
    # Agrégation par date
    daily_data = df.groupby('date').agg({
        'interaction_id': 'count',
        'est_achat': 'sum',
        'valeur_achat': 'sum'
    }).reset_index()
    
    daily_data.rename(columns={
        'interaction_id': 'nb_interactions',
        'est_achat': 'nb_achats'
    }, inplace=True)
    
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=daily_data['date'],
        y=daily_data['nb_interactions'],
        name='Interactions',
        line=dict(color='blue')
    ))
    fig_trend.add_trace(go.Scatter(
        x=daily_data['date'],
        y=daily_data['nb_achats'],
        name='Achats',
        line=dict(color='red')
    ))
    fig_trend.update_layout(title="Évolution des Interactions et Achats")
    st.plotly_chart(fig_trend, use_container_width=True)

    # ===== TABLEAU DE DONNÉES =====
    st.header("📋 Aperçu des Données")
    
    with st.expander("Voir les données brutes"):
        st.dataframe(df.head(100))

    # ===== FOOTER =====
    st.markdown("---")
    st.markdown(
        "**Dashboard développé pour Numberly** • "
        "Données synthétiques générées avec Faker • "
        "Stack technique: Python, Pandas, Streamlit, Plotly"
    )
else:
    st.error("❌ Données non disponibles. Exécutez d'abord: python etl_pipeline.py")