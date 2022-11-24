#DEBUT

#On admet la fonction input() qui renvoi la valeur donnée par l'utilisateur
#On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe

#Définir une fonction pierreFeuilleCiseaux qui lance une partie
    #Ecrire "Ce jeu est un pierre feuille ciseaux. Choisissez la bonne option pour vaincre votre adversaire. Chaque manche gagnée rapporte 1 point. Le jeu se termine quand vous ou l'adversaire atteint 2 points."
    #Initialiser une variable scorePlayer à 0
    #Initialiser une variable scoreCpu à 0
    #Tant que scorePlayer inférieur à 2 ou scoreCpu inférieur à 2:
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Choisis ce que tu veux faire : 0 pour pierre, 1 pour feuille, 2 pour ciseaux :")"
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction random()
        #Ecrire "Mon choix est :", cpuChoice

        #si cpuChoice est égal à playerChoice
            #Ecrire "Egalité."

        #Si playerChoice égal 0 et cpuChoice égal 1 ou playerChoice égal 1 et cpuChoice 2 ou playerChoice 2 égal et cpuChoice égal 0
            #Ecrire "Victoire!"
            #Incrémenter scorePlater de 1

        #Si playerChoice égal 1 et cpuChoice égal 0 ou playerChoice égal 2 et cpuChoice 1 ou playerChoice 0 égal et cpuChoice égal 2
            #Ecrire "Défaite!"
            #Incrémenter scoreCpu de 1

        #Sinon playerChoice ne renvoi à aucun index de game
            #Ecrire "Choix impossible!"
            #Passer à l'itération suivante de la boucle
        
    #Si scorePlayer égal à 2:
        #Ecrire scorePlayer"/"scoreCpu ". Vous avez gagné."
        
    #Sinon scoreCPU égal à 2:
        #Ecrire scoreCpu"/"scorePlayer ". Vous avez perdu."   
        

#Executer la fonction pierreFeuilleCiseaux



#FIN
