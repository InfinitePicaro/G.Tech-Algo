import copy

#Lance une partie où l'IA/Cortana gagne à chaque fois ou fait une égalité
def impossibleMorpion():

    #Initialise le tableau 3X3
    tab = [ ["_" for i in range(3)] for i in range(3) ]
    #Définir un dictionnaire dans lequel on stock les noms des joueurs
    curPlayer = {
        1: "Joueur",
        -1: "Cortana"
    }

    #Initialiser une variable curPlayerID égale à 1 dans laquelle on définit l'ID du joueur actuel
    curPlayerID = 1

    #Définir un dictionnaire dans lequel on stock les symboles des joueurs en fonction de leur ID
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    #Rentrer la première action de l'IA/Cortana
    tab[1][1] = "X"
    #Créer une variable action égale à1 dans laquelle on défini le nombre d'actions passées depuis le début de la partie
    action = 1

    #Tant que True
    while True:

        #Pour i dans tab
        for i in tab:
            #Ecrire i
            print(i)

        #Incrémenter action de 1
        action += 1

        #Si curPlayerID est égal à 1
        if curPlayerID == 1:
            #Définir une variable boolean choix à False
            choix = False
            #Tant que choix n'est pas vrai
            while not choix:
                #Ecrire "C'est à toi de jouer !"
                print("C'est à toi de jouer !")
                #Définir la variable choixX avec comme valeur le retour de l'éxecution de la fonction input("Ligne :")
                choixX = int(input("Ligne (1 à 3) : ")) - 1
                #Définir la variable choixY avec comme valeur le retour de l'éxecution de la fonction input("Colonne :")
                choixY = int(input("Colonne (1 à 3) : ")) - 1
                #Si l'index de tab correspondant à [choixX][choixY] est différent du caractère "_"
                if tab[choixX][choixY] != "_":
                    #Ecrire "Case occupée, fais un autre choix."
                    print("Case occupée, fais un autre choix.")
                #Sinon
                else:
                    #Afficher le symbole de curPlayerID à [choixX][choixY]
                    tab[choixX][choixY] = playerSymbole[curPlayerID]
                    #Assigner True à la variable choix
                    choix = True
        #Sinon
        else:
            #Ecrire "Au tour de Cortana"
            print("Au tour de Cortana")

        #Ecrire ""
        print("")
        #Si action est égal à 3 et curPlayerID est égal à -1
        if action == 3 and curPlayerID == -1:
            #Si la coordonnée [0][0] est égal à "_"
            if tab[0][0] == "_":
                #Assigner "X" au choix
                tab[0][0] = "X"
            #Sinon
            else:
                #Assigner à la cooordonnée tab[0][2] la valeur "X"
                tab[0][2] = "X"

        #Si action est égal à 5 et curPlayerID est égal à 1
        if action == 5 and curPlayerID == -1:
            #Définir une variable boolean check à False
            check = False
            #Pour x allant de 0 à 2
            for x in range(3):
                #Si check n'est pas vrai
                if not check:
                    #Pour y allant de 0 à 2
                    for y in range(3):
                        #Si tab[x][y] est égal au caractère "_"
                        if tab[x][y] == "_":
                            #Initialiser la variable tempTab avec comme valeur la copie de tab
                            tempTab = copy.deepcopy(tab)
                            #Assigner à la coordonnée tempTab[x][y] le symbole "O"
                            tempTab[x][y] = "O"
                            #Si l'une des conditions de victoire du Joueur est remplie
                            if (tempTab[0][0] == "O" and tempTab[0][1] == "O" and tempTab[0][2] == "O") or (tempTab[1][0] == "O" and tempTab[1][1] == "O" and tempTab[1][2] == "O") or (tempTab[2][0] == "O" and tempTab[2][1] == "O" and tempTab[2][2] == "O") or (tempTab[0][0] == "O" and tempTab[1][0] == "O" and tempTab[2][0] == "O") or (tempTab[0][1] == "O" and tempTab[1][1] == "O" and tempTab[2][1] == "O") or (tempTab[0][2] == "O" and tempTab[1][2] == "O" and tempTab[2][2] == "O") or (tempTab[0][0] == "O" and tempTab[1][1] == "O" and tempTab[2][2] == "O") or (tempTab[0][2] == "O" and tempTab[1][1] == "O" and tempTab[2][0] == "O"):
                                #Assigner aux coordonnées tab[x][y] la valeur "X"
                                tab[x][y] = "X"
                                #Modifier check pour check égal True
                                check = True
                                #Casser la boucle
                                break
            #Si check n'est pas vrai et tab[2][2] est égal à "_"
            if not check and tab[2][2] == "_":
                #Assigner à la coordonnée tab[2][2] la valeur "X"
                tab[2][2] = "X"
            #Sinon si check n'est pas vrai
            elif not check:
                #Assigner à la coordonnée tab[2][0] la valeur "X"
                tab[2][0] = "X"
        
        #Si action est égal à 7
        if action == 7:
            #Définir une variable boolean check à False
            check = False
            #Pour x allant de 0 à 2
            for x in range(3):
                #Si check n'est pas vrai
                if not check:
                    #Pour y allant de 0 à 2
                    for y in range(3):
                        #Si la coordonnée tab[x][y] est égal à la valeur "_"
                        if tab[x][y] == "_":
                            #Initialiser la variable tempTab avec comme valeur la copie de tab
                            tempTab = copy.deepcopy(tab)
                             #Assigner à la coordonnée tempTab[x][y] le symbole "X"
                            tempTab[x][y] = "X"
                            #Si l'une des conditions de victoire de l'IA/Cortana est remplie
                            if (tempTab[0][0] == "X" and tempTab[0][1] == "X" and tempTab[0][2] == "X") or (tempTab[1][0] == "X" and tempTab[1][1] == "X" and tempTab[1][2] == "X") or (tempTab[2][0] == "X" and tempTab[2][1] == "X" and tempTab[2][2] == "X") or (tempTab[0][0] == "X" and tempTab[1][0] == "X" and tempTab[2][0] == "X") or (tempTab[0][1] == "X" and tempTab[1][1] == "X" and tempTab[2][1] == "X") or (tempTab[0][2] == "X" and tempTab[1][2] == "X" and tempTab[2][2] == "X") or (tempTab[0][0] == "X" and tempTab[1][1] == "X" and tempTab[2][2] == "X") or (tempTab[0][2] == "X" and tempTab[1][1] == "X" and tempTab[2][0] == "X"):
                                #Assigner aux coordonnées tab[x][y] la valeur "X"
                                tab[x][y] = "X"
                                #Modifier check pour check égal True
                                check = True
                                #Casser la boucle
                                break
            #Si check n'est pas vrai
            if not check:
                #Modifier check avec False
                check = False
                #Pour x allant de 0 à 2
                for x in range(3):
                    #Si check n'est pas vrai
                    if not check:
                        #Pour y allant de 0 à 2
                        for y in range(3):
                            #Si tab[x][y] est égal à la valeur "_"
                            if tab[x][y] == "_":
                                #Assigner aux coordonnées tab[x][y] la valeur "X"
                                tab[x][y] = "X"
                                #Modifier check pour check égal True
                                check = True
                                #Casser la boucle
                                break
        
        #Si action est égal à 9
        if action == 9:
            #Définir une variable boolean check à False
            check = False
            #Pour x allant de 0 à 2
            for x in range(3):
                #Si check n'est pas vrai
                if not check:
                    #Pour y allant de 0 à 2
                    for y in range(3):
                        #Si tab[x][y] est égal à la valeur "_"
                        if tab[x][y] == "_":
                            #Assigner aux coordonnées tab[x][y] la valeur "X"
                            tab[x][y] = "X"
                            #Modifier check pour check égal True
                            check = True
                            #Casser la boucle
                            break

        #Intialiser une vraiable cur égal au symbole de l'ID du joueur actuel
        cur = playerSymbole[curPlayerID]
        #Si l'une des conditions de victoire est remplie
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            #Pour i dans tab
            for i in tab:
                #Ecrire i
                print(i)
            #Ecrire "{curPlayer[curPlayerID]} a gagné"
            print(f"{curPlayer[curPlayerID]} a gagné")
            #Casser la boucle
            break
        #Sinon si action est égal à 9
        elif action == 9:
            #Ecrire "Egalité..."
            print("Egalité...")
            #Casser la boucle
            break
        
        #Multiplier la variable curPlayerID par -1
        curPlayerID = curPlayerID * -1

#Exécuter la fonction impossibleMorpion
impossibleMorpion()