from pymongo import MongoClient

# connexion à MongoDB ( a refaire)
connexion = MongoClient("mongodb://localhost:27017/")
database = connexion["AmirGameDB"]

# création des collections si elles n'existent pas déjà
if "Monstres" not in database.list_collection_names():
    database.create_collection("Monstres")

if "Joueurs" not in database.list_collection_names():
    database.create_collection("Joueurs")

# liste des monstres
liste_monstres = [
    {"name": "Gobelin", "attack": 10, "defense": 5, "hp": 50},
    {"name": "Orc", "attack": 20, "defense": 8, "hp": 120},
    {"name": "Dragon", "attack": 35, "defense": 20, "hp": 300},
    {"name": "Zombie", "attack": 12, "defense": 6, "hp": 70},
    {"name": "Troll", "attack": 25, "defense": 15, "hp": 200},
    {"name": "Spectre", "attack": 18, "defense": 10, "hp": 100},
    {"name": "Golem", "attack": 30, "defense": 25, "hp": 250},
    {"name": "Vampire", "attack": 22, "defense": 12, "hp": 150},
    {"name": "Loup-garou", "attack": 28, "defense": 18, "hp": 180},
    {"name": "Squelette", "attack": 15, "defense": 7, "hp": 90}
]

# liste des joueurs
liste_joueurs = [
    {"name": "Mellina", "attack": 10, "defense": 5, "hp": 50},
    {"name": "Ines", "attack": 20, "defense": 8, "hp": 120},
    {"name": "Hamza", "attack": 35, "defense": 20, "hp": 300},
    {"name": "Robin", "attack": 12, "defense": 6, "hp": 70},
    {"name": "Aminec", "attack": 25, "defense": 15, "hp": 200},
    {"name": "Guigui", "attack": 18, "defense": 10, "hp": 100},
    {"name": "Pol", "attack": 30, "defense": 25, "hp": 250},
    {"name": "Moha", "attack": 22, "defense": 12, "hp": 150},
    {"name": "Amire", "attack": 28, "defense": 18, "hp": 180},
    {"name": "Amine", "attack": 15, "defense": 7, "hp": 90}
]

# récupération des collections
col_joueurs = database["Joueurs"]
col_monstres = database["Monstres"]

# suppression des anciennes données
col_joueurs.delete_many({})
col_monstres.delete_many({})

# insertion des données
col_joueurs.insert_many(liste_joueurs)
col_monstres.insert_many(liste_monstres)

print("Joueurs ajoutés :", col_joueurs.count_documents({}))
print("Monstres ajoutés :", col_monstres.count_documents({}))

# affichage des collections présentes
print("\nCollections disponibles :", database.list_collection_names())

# affichage des joueurs
print("\nListe des joueurs :")
for joueur in col_joueurs.find():
    print(f"{joueur['name']} -> HP:{joueur['hp']} ATK:{joueur['attack']} DEF:{joueur['defense']}")

# affichage des monstres
print("\nListe des monstres :")
for monstre in col_monstres.find():
    print(f"{monstre['name']} -> HP:{monstre['hp']} ATK:{monstre['attack']} DEF:{monstre['defense']}")

print("\nBase de données chargée avec succès.")