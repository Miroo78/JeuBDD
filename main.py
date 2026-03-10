# 09/03 version squeltte 

# fonction decouper en plusieurs fonctions pour une meilleure organisation du code et une meilleure lisibilité

def afficher_menu(): # Afficher le menu principl 
    print("1. Démarrer le jeu")
    print("2. Classement")
    print("3. Quitter")


def demarrer_jeu(): # Démarrer le jeu
    print("Le jeu démarre nchalah...")


def afficher_classement(): # Afficher le classement des joueurs
    print("Voici le classement des jpuers : Amir : 32 secondes, Yassine : 45 secondes, Anas : 50 secondes")


def recuperer_choix_valide(): # Récupérer le choix de l'utilisateur et vérifier sa validité
    while True:
        choix = input("Ton choix : ")
        if choix in ["1", "2", "3"]:
            return int(choix)
        else:
            print("Choix invalide, veuillez réessayer.")

def lancer_choix_choisi(choix):
    if choix == 1:
        demarrer_jeu()
    elif choix == 2:
        afficher_classement()
    elif choix == 3:
        print("Au revoir")            



def main(): 
    # Afficher le menu de choix
    afficher_menu()

    # Récupérer le choix de l'utilisateur valide
    choix = recuperer_choix_valide()

    # Gérer les choix de l'utilisateur
    lancer_choix_choisi(choix)

main()