import pandas as pd
import numpy as np

def generate_marketing_data():
    fake = Faker()
    np.random.seed(42)


# Données clients 
    #Initialise une liste de clients vide
    clients = []
    
      #- Boucle qui s’exécute 1000 fois pour créer 1000 clients.
    for i in range(1000):
        clients.append({
            'client_id': f"C_{i:04d}",         #Identifiant unique du client avec 4 chiffres,
            'age': np.random.randint(18, 65),    #Âge aléatoire entre 18 et 65,
            'ville': fake.city(),            #Nom de la ville généré aléatoirement,
            'segment': np.random.choice(['Premium', 'Standard', 'Basique']),       #Segment choisi aléatoirement parmi trois options,
            'canal_acquisition': np.random.choice(['Partenariat', 'SEO', 'Publicité', 'Affiliation', 'Email', 'Direct'])    #Canaux d’acquisition choisi logiquement pour attirer les clients
        })
    

    # Données générées interactions entre des clients et un site ou une application  
    # Initialise une liste vide pour stocker les interactions.
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

#préparer les données d’interactions clients pour une analyse.
 
def transform_data(df_clients, df_interactions):
    df_merged = pd.merge(df_interactions, df_clients, on='client_id')
    df_merged['est_achat'] = df_merged['valeur_achat'] > 0
    df_merged['date'] = pd.to_datetime(df_merged['date'])
    return df_merged

if __name__ == "__main__":
    print("Génération des données marketing...")
    clients, interactions = generate_marketing_data()
    df_final = transform_data(clients, interactions)
    
    
    
if __name__ == "__main__":
    print(" Génération des données marketing...")
    clients, interactions = generate_marketing_data()
    df_final = transform_data(clients, interactions)
    
    df_final.to_csv('donnees_marketing.csv', index=False)
    clients.to_csv('clients.csv', index=False)
    
    print(" Données sauvegardées : donnees_marketing.csv")
    print(f"{len(df_final)} lignes générées")
    