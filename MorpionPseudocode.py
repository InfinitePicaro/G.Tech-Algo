# on admet la fonction input() qui renvoie la valeur donné par l'utilisateur.
# on admet la fonction randint() qui renvoie une valeur comprise entre deux entiers donné en parametre.
from random import randint

# definir une fonction morpion() qui lance une partie de morpion entre deux joueurs.
    # definir un tableau de 3 x 3 avec des symboles vide.

    # définir bullet avec comme valeur 1

    # définir un dictionaire dans lequel on stock le nom des joueurs
    # definir une variable à laquelle on assigne l'ID du joueur actuel
    # definir un dictionaire dans lequel on stock le symbole de chaque joueur en fonction de son ID

    # tant que True
        # définir la variable booléenne check à False
        # tant que check n'est pas égal à True
            # écrire le nom du joueur dont c'est le tour en fonction de l'ID du joueur actuel dans curPlayer 

            # on assigne à la variable choixX le retour de la variable input("Ligne (1 à 3): ") sous forme d'entier
            # on assigne à la variable choixX le retour de la variable input("Colonne (1 à 3): ") sous forme d'entier

            # si choixX et choixY sont égal à -1 et que bullet égal 1
                # check égal True
                #assigner à une variable x1 une valeur aléatoire entre 0 et 2
                #assigner à une variable y1 une valeur aléatoire entre 0 et 2
                #Assigner à une variable x2 la valeur None
                #Assigner à une variable y2 la valeur None
                #Tant que x1 est différent de x2 et y1 est différent de y2
                    #Assigner à la variable x2 une valeur aléatoire entre 0 et 2
                    #Assigner à la variable y2 une valeur aléatoire entre 0 et 2
                #Ecrire x1 et y1
                #Ecrire x2 et y2
                #Assigner aux coordonnées x1 y1 le symbole lié à l'ID du joueur actuel dans curPlayer
                #Assigner aux coordonnées x2 y2 le symbole lié à l'ID du joueur actuel dans curPlayer
                #Chnager l'ID du joueur actuel dans curPlayerID
                #Soustraire 1 à bullet

            # sinon si choixX et choixY sont égal à -1 et que bullet n'est pas égal à 1
                # alors on ecrit "à court de balle...".

            # sinon si les valeurs de choixX et choixY ne sont pas dans le tableau ou que tab[choixX-1][choixY-1] est different de "_".
                # alors on ecrit "case occupée, fais un autre choix".
            
            # sinon
                # assigner le symbole du joueur aux coordonnées choixX, choixY dans tab.
                #Assigner la valeur True à check

        # pour chaque element de tab
            # on écrit la ligne du tableau

        # on stock temporairement le symbole du joueur actuel dans la variable cur.
        # si l'action du joueur est un action qui lui fait gagner la partie.
            # alors on ecrit quel joueur à gagné
            # puis on force la sortie de la boucle infinie avec un break
        
        # si tab[choixX-1][choixY-1] est égal au symbole du joueur.
            # alors on change l'ID de curPlayerID en multipliant la variable par -1.

#Exécuter la fonction morpion