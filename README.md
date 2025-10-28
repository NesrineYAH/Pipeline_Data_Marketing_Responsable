<!DOCTYPE html>
<html>
<head>
    <title>Numberly - Pipeline Data Marketing</title>
</head>
<body>
    <h1>🚀 Numberly - Pipeline Data Marketing Responsable</h1>
    <p><strong>Pipeline ETL + Dashboard pour l'analyse de données marketing respectueuse de la vie privée</strong></p>

    <h2>📋 Table des Matières</h2>
    <ul>
        <li><a href="#objectif">🎯 Objectif</a></li>
        <li><a href="#architecture">🏗️ Architecture</a></li>
        <li><a href="#technologies">🛠️ Technologies</a></li>
        <li><a href="#installation">🚀 Installation</a></li>
        <li><a href="#utilisation">📊 Utilisation</a></li>
        <li><a href="#fonctionnalites">🎨 Fonctionnalités</a></li>
        <li><a href="#structure">📁 Structure du Projet</a></li>
    </ul>

    <h2 id="objectif">🎯 Objectif</h2>
    <p>Simuler un pipeline data engineering complet pour Numberly, spécialiste du Data Marketing, en mettant en œuvre :</p>
    <ul>
        <li><strong>Génération de données synthétiques</strong> respectueuses de la vie privée</li>
        <li><strong>Pipeline ETL</strong> (Extract, Transform, Load) robuste</li>
        <li><strong>Dashboard interactif</strong> pour l'analyse marketing</li>
        <li><strong>Containerisation Docker</strong> pour la reproductibilité</li>
    </ul>

    <h2 id="architecture">🏗️ Architecture</h2>
    <pre>
📥 Génération Données → 🔄 Transformation ETL → 💾 Sauvegarde CSV → 📊 Dashboard Streamlit
    </pre>

    <h2 id="technologies">🛠️ Technologies</h2>
    <h3>Backend</h3>
    <ul>
        <li>Python</li>
        <li>Pandas</li>
        <li>Faker</li>
    </ul>

    <h3>Visualisation</h3>
    <ul>
        <li>Streamlit</li>
        <li>Plotly</li>
    </ul>

    <h3>Containerisation</h3>
    <ul>
        <li>Docker</li>
        <li>Docker Compose</li>
    </ul>

    <h2 id="installation">🚀 Installation</h2>

    <h3>Méthode 1 : Avec Docker (Recommandé)</h3>
    <pre><code>
# Cloner le repository
git clone <votre-repo>
cd Numberly_Pipeline_Data_Marketing_Responsable

# Lancer avec Docker Compose
docker-compose up
    </code></pre>

    <h3>Méthode 2 : Manuellement</h3>
    <pre><code>
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
    </code></pre>

    <h2 id="utilisation">📊 Utilisation</h2>

    <h3>1. Génération des Données</h3>
    <pre><code>python etl_pipeline.py</code></pre>
    <p>📈 <strong>Résultat :</strong> 1 000 clients et 5 000 interactions générées</p>

    <h3>2. Lancement du Dashboard</h3>
    <pre><code>streamlit run dashboard/streamlit_app.py</code></pre>
    <p>🌐 <strong>Accès :</strong> http://localhost:8501</p>

    <h3>3. Avec Docker</h3>
    <pre><code>
# Lancer uniquement l'ETL
docker-compose run etl-pipeline

# Lancer uniquement le dashboard
docker-compose up dashboard

# Tout lancer
docker-compose up
    </code></pre>

    <h2 id="fonctionnalites">🎨 Fonctionnalités</h2>

    <h3>📈 Dashboard Analytics</h3>
    <ul>
        <li><strong>KPIs Principaux</strong> : Clients uniques, taux de conversion, chiffre d'affaires</li>
        <li><strong>Performance par Canal</strong> : SEO, Social, Email, Direct</li>
        <li><strong>Segmentation Clients</strong> : Premium, Standard, Basique</li>
        <li><strong>Analyse Temporelle</strong> : Évolution des interactions et achats</li>
        <li><strong>Visualisations Interactives</strong> : Graphiques Plotly</li>
    </ul>

    <h3>🔧 Pipeline Data</h3>
    <ul>
        <li><strong>Génération de données réalistes</strong> avec Faker</li>
        <li><strong>Nettoyage et transformation</strong> des données</li>
        <li><strong>Calcul de métriques business</strong> (RFM, conversion, etc.)</li>
        <li><strong>Export format CSV</strong> pour analyse ultérieure</li>
    </ul>

    <h2 id="structure">📁 Structure du Projet</h2>
    <pre>
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
    </pre>

    <h2>📊 Jeu de Données</h2>

    <h3>Données Générées</h3>
    <ul>
        <li><strong>1 000 clients</strong> avec :
            <ul>
                <li>Démographie (âge, ville)</li>
                <li>Segment (Premium, Standard, Basique)</li>
                <li>Canal d'acquisition</li>
            </ul>
        </li>
        <li><strong>5 000 interactions</strong> avec :
            <ul>
                <li>Types d'actions (page_vue, ajout_panier, achat)</li>
                <li>Valeurs d'achat</li>
                <li>Timestamps réalistes</li>
            </ul>
        </li>
    </ul>

    <h2>👨‍💻 Auteur</h2>
    <p>Développé avec ❤️ pour Numberly dans le cadre d'une recherche d'alternance Data Engineer/Data Analyst.</p>
    <p><em>"Transformer la data en insights actionnables"</em> 🚀</p>

</body>
</html>