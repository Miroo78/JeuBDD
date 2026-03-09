# 09/03 version squeltte 
def afficher_menu():
    print("1. Démarrer le jeu")
    print("2. Classement")
    print("3. Quitter")


def demarrer_jeu():
    print("Le jeu démarre...")


def afficher_classement():
    print("Classement )")


def main():
    afficher_menu()
    choix = input("Ton choix : ")

    if choix == "1":
        demarrer_jeu()
    elif choix == "2":
        afficher_classement()
    elif choix == "3":
        print("Au revoir")
    else:
        print("Choix invalide")


main()