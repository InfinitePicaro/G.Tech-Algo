#DEBUT

#On admet la fonction input() qui renvoi la valeur donnée par l'utilisateur
#On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe
from random import randint

#Définir une fonction pierreFeuilleCiseaux qui lance une partie
def pierreFeuilleCiseaux():
    #Ecrire "Ce jeu est un pierre feuille ciseaux. Choisissez la bonne option pour vaincre votre adversaire. Chaque manche gagnée rapporte 1 point. Le jeu se termine quand vous ou l'adversaire atteint 2 points."
    print("Choisissez la bonne option pour vaincre votre adversaire.")
    #Initialiser une variable scorePlayer à 0
    scorePlayer = 0
    #Initialiser une variable scoreCpu à 0
    scoreCpu = 0
    #Tant que scorePlayer inférieur à 2 ou scoreCpu inférieur à 2:
    while scorePlayer != 2 and scoreCpu != 2 :
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Choisis ce que tu veux faire : 0 pour pierre, 1 pour feuille, 2 pour ciseaux :")
        playerChoice = int(input("Choisis : 0 pour pierre, 1 pour feuille, 2 pour ciseaux :"))
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction random()
        cpuChoice = int(randint(0, 2))
        print("Mon choix est :", cpuChoice)

        #si cpuChoice est égal à playerChoice
        if cpuChoice == playerChoice:
            #Ecrire "Egalité."
            print("Egalité.")

        #Si playerChoice égal 0 et cpuChoice égal 1 ou playerChoice égal 1 et cpuChoice 2 ou playerChoice 2 égal et cpuChoice égal 0
        elif (playerChoice == 0 and cpuChoice == 1) or (playerChoice == 1 and cpuChoice == 2) or (playerChoice == 2 and cpuChoice == 0):
            #Ecrire "Victoire!"
            print("Défaite!")
            #Incrémenter scorePlater de 1
            scoreCpu += 1

        #Si playerChoice égal 1 et cpuChoice égal 0 ou playerChoice égal 2 et cpuChoice 1 ou playerChoice 0 égal et cpuChoice égal 2
        elif (playerChoice == 1 and cpuChoice == 0) or (playerChoice == 2 and cpuChoice == 1) or (playerChoice == 0 and cpuChoice == 2):
            #Ecrire "Défaite!"
            print("Victoire!")
            #Incrémenter scoreCpu de 1
            scorePlayer += 1

        #Sinon playerChoice ne renvoi à aucun index de game
        else:
            #Ecrire "Choix impossible!"
            print("Choix impossible!")
            pass
        
    #Si scorePlayer égal à 2:
    if scorePlayer == 2:
        #Ecrire scorePlayer"/"scoreCpu ". Vous avez gagné."
        print(scorePlayer, "/", scoreCpu, ". Vous avez gagné.")
        
    #Sinon scoreCPU égal à 2:
    else:
        #Ecrire scoreCpu"/"scorePlayer ". Vous avez perdu."
        print(scoreCpu, "/", scorePlayer, ". Vous avez perdu.")      
        

#Executer la fonction pierreFeuilleCiseaux
pierreFeuilleCiseaux()



#FIN


  