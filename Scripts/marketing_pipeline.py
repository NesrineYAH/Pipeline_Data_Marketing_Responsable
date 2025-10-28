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
    

    # Données interactions   
    interactions = []