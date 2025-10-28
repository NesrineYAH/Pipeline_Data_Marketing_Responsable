# 🚀 Numberly - Pipeline Data Marketing Responsable

**Pipeline ETL + Dashboard pour l'analyse de données marketing respectueuse de la vie privée**

---

## 📋 Table des Matières
- [🎯 Objectif](#-objectif)
- [🏗️ Architecture](#️-architecture)
- [🛠️ Technologies](#️-technologies)
- [🚀 Installation](#-installation)
- [📊 Utilisation](#-utilisation)
- [🎨 Fonctionnalités](#-fonctionnalités)
- [📁 Structure du Projet](#-structure-du-projet)
- [🤝 Contribution](#-contribution)

🤝 Contribution
Ce projet a été développé Nesrine YAHOUM Data Engineer, Développeuse full stack  pour démontrer des compétences en data engineering dans le cadre d'une candidature  dans le cadre d'une recherche d'alternance Data Engineer/Data Analystchez  Numberly.

<p><em>"Transformer la data en insights actionnables"</em> 🚀</p>

## 🎯 Objectif

Simuler un pipeline data engineering complet pour Numberly, spécialiste du Data Marketing, en mettant en œuvre :
- **Génération de données synthétiques** respectueuses de la vie privée
- **Pipeline ETL** (Extract, Transform, Load) robuste
- **Dashboard interactif** pour l'analyse marketing
- **Containerisation Docker** pour la reproductibilité

---

## 🏗️ Architecture

```mermaid
graph TB
    A[📥 Génération Données] --> B[🔄 Transformation ETL]
    B --> C[💾 Sauvegarde CSV]
    C --> D[📊 Dashboard Streamlit]
    E[🐳 Docker] --> A
    E --> D
    

##  Manuellement

- ** pip install -r requirements.txt
- ** python etl_pipeline.py
- ** streamlit run dashboard/streamlit_app.py

## Lancer uniquement l'ETL
docker-compose run etl-pipeline

##  Lancer uniquement le dashboard
docker-compose up dashboard

## Dashboard Analytics
- ** KPIs : Clients, Conversion, Chiffre d'affaires
- ** Performance par canal (SEO, Social, Email, Direct)
- **Segmentation clients (Premium, Standard, Basique)

<h2 id="fonctionnalites">🎨 Fonctionnalités</h2>

<h3>📈 Dashboard Analytics</h3>

KPIs Principaux : Clients uniques, taux de conversion, chiffre d'affaires
    Performance par Canal : SEO, Social, Email, Direct
    Segmentation Clients : Premium, Standard, Basique
    Analyse Temporelle: Évolution des interactions et achats
    Visualisations Interactives : Graphiques Plotly


<h3>🔧 Pipeline Data</h3>

 - ** Génération de données réalistes avec Faker
 - ** Nettoyage et transformation des données
 - ** Calcul de métriques business (RFM, conversion, etc.)
 - ** Export format CSV pour analyse ultérieure

<h2> 📁 Structure du Projet</h2>
<img src="./assets/structure projets.png" alt="structure projet" >








##  Visualisations interactives Plotly
<h2> 📊 Jeu de Données </h2>
Données Générées
1 000 clients avec :
- **
- ** Démographie (âge, ville)
- ** Segment (Premium, Standard, Basique)
- ** Canal d'acquisition

5 000 interactions avec :

- ** Types d'actions (page_vue, ajout_panier, achat)
- ** Valeurs d'achat
- ** Timestamps réalistes

Métriques Calculées
- ** Taux de conversion par canal
- ** Chiffre d'affaires total
Panier moyen
- ** Segmentation comportementale


Stack technique alignée sur les besoins Numberly :

✅ Python, SQL, ETL
✅ Docker, Containerisation
✅ Data Analysis, Visualisation
✅ Marketing Data responsable

## Pipeline Data
Génération 1 000 clients + 5 000 interactions

Calcul métriques business (RFM, conversion)

Export CSV pour analyse

🌐 Accès
Dashboard : http://localhost:8501

Données : Générées automatiquement dans data/