# etl_pipeline.py
import pandas as pd
import numpy as np
from faker import Faker

def generate_marketing_data():
    fake = Faker()
    np.random.seed(42)
    
    # Données clients
    clients = []
    for i in range(1000):
        clients.append({
            'client_id': f"C_{i:04d}",
            'age': np.random.randint(18, 65),
            'ville': fake.city(),
            'segment': np.random.choice(['Premium', 'Standard', 'Basique']),
            'canal_acquisition': np.random.choice(['SEO', 'Social', 'Email', 'Direct'])
        })
    
    # Données interactions
    interactions = []
    for i in range(5000):
        interactions.append({
            'interaction_id': i,
            'client_id': f"C_{np.random.randint(0, 1000):04d}",
            'type_action': np.random.choice(['page_vue', 'ajout_panier', 'achat']),
            'valeur_achat': np.random.uniform(10, 200) if np.random.random() > 0.7 else 0,
            'date': fake.date_between(start_date='-3months', end_date='today')
        })
    
    return pd.DataFrame(clients), pd.DataFrame(interactions)

def transform_data(df_clients, df_interactions):
    df_merged = pd.merge(df_interactions, df_clients, on='client_id')
    df_merged['est_achat'] = df_merged['valeur_achat'] > 0
    df_merged['date'] = pd.to_datetime(df_merged['date'])
    return df_merged

if __name__ == "__main__":
    print("🚀 Génération des données marketing...")
    clients, interactions = generate_marketing_data()
    df_final = transform_data(clients, interactions)
    
    df_final.to_csv('donnees_marketing.csv', index=False)
    clients.to_csv('clients.csv', index=False)
    
    print("✅ Données sauvegardées : donnees_marketing.csv")
    print(f"📊 {len(df_final)} lignes générées")