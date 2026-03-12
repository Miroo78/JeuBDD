import random # afin de pouvoir faire des choix aléatoires pour les monstres et les joueurs dans le jeu de combat

# liste des monstres
liste_monstres = [
    {"name": "Gobelin", "attack": 10, "defense": 5, "hp": 50},
    {"name": "Orc", "attack": 20, "defense": 8, "hp": 120},
    {"name": "Dragon", "attack": 35, "defense": 20, "hp": 300},
    {"name": "Zombie", "attack": 12, "defense": 6, "hp": 70},
    {"name": "Troll", "attack": 25, "defense": 15, "hp": 200},
]

# liste des joueurs
liste_joueurs = [
    {"name": "Mellina", "attack": 10, "defense": 5, "hp": 50},
    {"name": "Ines", "attack": 20, "defense": 8, "hp": 120},
    {"name": "Amiré", "attack": 35, "defense": 20, "hp": 300},
    {"name": "Amir", "attack": 12, "defense": 6, "hp": 70},
    {"name": "Aminec", "attack": 25, "defense": 15, "hp": 200},
]

#le 09/03 version squeltte fait sans ia rien du tt 
# fonction dec en plusieurs fonctions pour une meilleure orga du code et une meilleure lisibilité

#-------------------------------------------------gestion menu-------------------------------------

def bienvenue(): # Afficher un message de bienvenue et demander à l'utilisateur de lancer le jeu avc A sinon le jeu se ferme
    print("Bienvenue dans le jeu de combat entre joueurs et monnstres ! cliquez sur A pour Lancer ")
    if input().lower() == 'a':
        print("Lancement du jeu...")
    else :
        print("Choix invalid, le jeu va se fermeer cheh .")
        exit()


def afficher_menu(): # Afficher le menu principl 
    print("1. Démarrer le jeu")
    print("2. Classement")
    print("3. Quitter")


def demarrer_jeu():
    username = input("Entrez votre nom : ")
    print(f"Bonjour {username} !")
    equipe = creer_equipe()
    print("\nVotre équipe est prête !")

    for joueur in equipe:
        print(joueur["name"])
    combat(equipe)



def afficher_classement(): # Afficher le classement des joueurs
    print("Voici le classement des jpuers : Amir : 32 secondes, Yassine : 45 secondes, Anas : 50 secondes")


#-------------------------------------------------gestion menu-------------------------------------

def recuperer_choix_valide(): # Récupérer le choix de l'utilisateur et vérifier sa validité
    while True:
        choix = input("Ton choix : ")
        if choix in ["1", "2", "3"]:
            return int(choix)
        else:
            print("Choix invalide, veuillez réessayer.")

def lancer_choix_choisi(choix): # Lancer la fonction correspdt au choix de luser
    if choix == 1:
        demarrer_jeu()
    elif choix == 2:
        afficher_classement()
    elif choix == 3:
        print("Au revoir") 
        
#-------------------------------------------------gestion equipe-------------------------------------

def afficher_joueurs_disponibles(joueurs):
    print("\nPersonnages disponibles :")
    for i, joueur in enumerate(joueurs):
        print(i + 1, "-", joueur["name"], ) 


def demander_choix_joueur(max_index):
    while True:
        try:
            choix = int(input("Choisissez un personnage : ")) - 1
            if 0 <= choix < max_index:
                return choix
            else:
                print("Choix invalide")
        except:
            print("Entrez un nombre valide")
        

def creer_equipe():
    joueurs_disponibles = liste_joueurs.copy()
    equipe = []

    while len(equipe) < 3:
        afficher_joueurs_disponibles(joueurs_disponibles)
        choix = demander_choix_joueur(len(joueurs_disponibles))
        joueur_choisi = joueurs_disponibles.pop(choix)
        equipe.append(joueur_choisi)
        print(joueur_choisi["name"], "ajouté à l'équipe")

    return equipe
#-------------------------------------------------gestion combat----------------------------------------------
def get_monstre_aleatoire():
    monstre = random.choice(liste_monstres)
    return monstre.copy()

def calculer_degats(attacker, defender):
    degats = attacker["attack"] - defender["defense"]
    if degats < 1:
        degats = 1
    return degats

def attaquer(attacker, defender):
    degats = calculer_degats(attacker, defender)
    defender["hp"] -= degats
    print(attacker["name"], "attaque", defender["name"], "et inflige", degats, "degats")

def get_joueur_vivant(equipe):

    for joueur in equipe:
        if joueur["hp"] > 0:
            return joueur
    return None

def combat(equipe):
    monstre = get_monstre_aleatoire()
    print("\nUn", monstre["name"], "apparait !")
    while monstre["hp"] > 0:

        joueur = get_joueur_vivant(equipe)
        if joueur is None:
            print("Tous les joueyurs sont morts !")
            return

        attaquer(joueur, monstre)
        if monstre["hp"] <= 0:
            print(monstre["name"], "est vaincu !")
            return

        attaquer(monstre, joueur)
        if joueur["hp"] <= 0:
            print(joueur["name"], "est mort !")


#-------------------------------------------------gestion main deroulment-------------------------------------
def main(): 
   # Afficher un message de bienvenue
    bienvenue() 

    # Afficher le menu de choix
    afficher_menu()

    # Récupérer le choix de l'utilisateur valide
    choix = recuperer_choix_valide()

    # Gérer les choix de l'utilisateur
    lancer_choix_choisi(choix)

main()