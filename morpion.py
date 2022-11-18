#on admet la fonction input() qui renvoi la valeur donnée par l'utilisateur

#Définir une fonction morpion() qui une partie de morpion entre deux joueurs
def morpion():
    #Définir un tableau de 3 x 3 avec un caractère "_" pour chacun des indexs
    tab = [ ["_" for i in range(3)] for i in range(3) ]
    #Définir un dictionnaire dans lequel on stock les noms des joueurs
    curPlayer = {
        1: "Joueur 1",
        -1: "Joueur 2"
    }
    #Créer une variable curPlayerID égale à 1 dans laquelle on définit l'ID du joueur actuel
    curPlayerID = 1
    #Définir un dictionnaire dans lequel on stock les symboles des joueurs en fonction de leur ID
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    #Tant que True
    while True:
        #Définir la variable booléenne check à False
        check = False
        #Tant que check n'est pas vrai
        while not check:
            #Ecrire le nom du joueur dont c'est le tor en fonction de l'ID du joueur actuel dans curPlayer
            print(f"{curPlayer[curPlayerID]}, c'est à toi !")

            #Définir la variable choixX avec comme valeur le retour de l'éxecution de la fonction int(input"coordonné x : "))
            choixX = int(input("coordonné x : "))
            #Définir la variable choixY avec comme valeur le retour de l'éxecution de la fonction int(input("coordonné y : "))
            choixY = int(input("coordonné y : "))

            #Si tab[choixX][choixY] est différent du caractère "_"
            if tab[choixX][choixY] != "_":
                #Ecrire "Case occupée, fais un autre choix."
                print("Case occupée, fais un autre choix.")
            
            #Sinon
            else:
                #Assigner le symbole du joueur aux cordonnées choixX, choixY dans tab
                tab[choixX][choixY] = playerSymbole[curPlayerID]
                check = True

        #Pour chaque élément dans tab
        for i in tab:
            #Ecrire la ligne du tableau
            print(i)

        #on stock temporairement le symbole du joueur actuel dans la variable cur
        cur = playerSymbole[curPlayerID]
        #Si l'une des conditions de victoire est remplie
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            #Alors écrire curPlayer[curPlayerID]"a gagné."
            print(f"{curPlayer[curPlayerID]} a gagné.")
            #Puis on force la sortie de la boucle infinie avec un break 
            break
        
        #Si tab[choixX][choixY] est égal au symbole du joueur
        if tab[choixX][choixY] == playerSymbole[curPlayerID]:
            #Alors on change l'ID du joueur en multipliant le variable par -1
            curPlayerID = curPlayerID * -1

#Exécuter la fonction morpion
morpion()


#Régler problème jeu avance quand même quand on met sur noptre propre symbole sur une case déjà occupée