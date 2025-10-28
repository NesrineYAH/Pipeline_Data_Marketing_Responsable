# 🚀 Numberly - Pipeline Data Marketing Responsable

**Pipeline ETL + Dashboard pour l'analyse de données marketing respectueuse de la vie privée**

---

## 📋 Table des Matières
<ul>
<li>
<a href=#>
</li>
- [🎯 Objectif]
- [🏗️ Architecture]
- [🛠️ Technologies]
- [🚀 Installation
- [📊 Utilisation]
- [🎨 Fonctionnalités](#-fonctionnalités)
- [📁 Structure du Projet](#-structure-du-projet)
- [🤝 Contribution](#-contribution)
<ul>
---
<h1>id="## 🎯Objectif"</h1>
 

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
🛠️ Technologies
Catégorie	Technologies
Backend	Python, Pandas, Faker
Visualisation	Streamlit, Plotly
Containerisation	Docker, Docker Compose
Data	CSV, Données synthétiques
🚀 Installation
Méthode 1 : Avec Docker (Recommandé)
bash
# Cloner le repository
git clone <votre-repo>
cd Numberly_Pipeline_Data_Marketing_Responsable

# Lancer avec Docker Compose
docker-compose up
Méthode 2 : Manuellement
bash
# Créer l'environnement virtuel
python -m venv numberly_env
source numberly_env/bin/activate  # Linux/Mac
numberly_env\Scripts\activate    # Windows

# Installer les dépendances
pip install -r requirements.txt

# Générer les données
python etl_pipeline.py

# Lancer le dashboard
streamlit run dashboard/streamlit_app.py
📊 Utilisation
1. Génération des Données
bash
python etl_pipeline.py
📈 Résultat : 1 000 clients et 5 000 interactions générées

2. Lancement du Dashboard
bash
streamlit run dashboard/streamlit_app.py
🌐 Accès : http://localhost:8501

3. Avec Docker
bash
# Lancer uniquement l'ETL
docker-compose run etl-pipeline

# Lancer uniquement le dashboard
docker-compose up dashboard

# Tout lancer
docker-compose up
🎨 Fonctionnalités
📈 Dashboard Analytics
KPIs Principaux : Clients uniques, taux de conversion, chiffre d'affaires

Performance par Canal : SEO, Social, Email, Direct

Segmentation Clients : Premium, Standard, Basique

Analyse Temporelle : Évolution des interactions et achats

Visualisations Interactives : Graphiques Plotly

🔧 Pipeline Data
Génération de données réalistes avec Faker

Nettoyage et transformation des données

Calcul de métriques business (RFM, conversion, etc.)

Export format CSV pour analyse ultérieure

📁 Structure du Projet
text
Numberly_Pipeline_Data_Marketing_Responsable/
│
├── 📊 etl_pipeline.py              # Script ETL principal
├── 🎨 dashboard/
│   └── streamlit_app.py           # Application Dashboard
├── 📁 data/                       # Données générées (CSV)
├── 📁 database/                   # Schémas SQL (futur)
├── 🐳 docker-compose.yml          # Orchestration Docker
├── 📦 Dockerfile                  # Configuration Container
├── 📋 requirements.txt            # Dépendances Python
└── 📖 README.md                   # Documentation
📊 Jeu de Données
Données Générées
1 000 clients avec :

Démographie (âge, ville)

Segment (Premium, Standard, Basique)

Canal d'acquisition

5 000 interactions avec :

Types d'actions (page_vue, ajout_panier, achat)

Valeurs d'achat

Timestamps réalistes

Métriques Calculées
Taux de conversion par canal

Chiffre d'affaires total

Panier moyen

Segmentation comportementale

🤝 Contribution
Ce projet a été développé pour démontrer des compétences en data engineering dans le cadre d'une candidature pour Numberly.

Stack technique alignée sur les besoins Numberly :

✅ Python, SQL, ETL

✅ Docker, Containerisation

✅ Data Analysis, Visualisation

✅ Marketing Data responsable

📄 Licence
Projet éducatif développé pour Numberly - © 2024

👨‍💻 Auteur
Développé avec ❤️ pour Numberly dans le cadre d'une recherche d'alternance Data Engineer/Data Analyst.

"Transformer la data en insights actionnables" 🚀

text

---

## 🎯 **CE QUE CE README APPORTE :**

✅ **Professionnel** et aligné avec Numberly  
✅ **Démontre vos compétences** techniques  
✅ **Guide d'installation** clair  
✅ **Structure bien documentée**  
✅ **Prêt pour GitHub** et les recruteurs  

**Ajoutez-le à votre projet et votre repo GitHub sera parfait !** 😊