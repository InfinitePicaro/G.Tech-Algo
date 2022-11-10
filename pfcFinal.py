#DEBUT

#On admet la fonction input() qui renvoi la valeur donnée par l'utilisateur
#On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe

#Définir une fonction pierreFeuilleCiseaux qui lance une partie
    #Ecrire "Ce jeu est un pierre feuille ciseaux. Choisissez la bonne option pour vaincre votre adversaire. Chaque manche gagnée rapporte 1 point. Le jeu se termine quand vous ou l'adversaire atteint 2 points."
    #Créer un tableau game = ["pierre","feuille","ciseaux"]
    #Initialiser une variable scorePlayer à 0
    #Initialiser une variable scoreCpu à 0
    #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Choisis ce que tu veux faire : 0 pour pierre, 1 pour feuille, 2 pour ciseaux :")
    #Ecrire "Vous avez choisi", game[playerChoice]
    #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction random()
    #Tant que scorePlayer inférieur à 2 ou scoreCpu inférieur à 2:
        
        #Si playerChoice a un choix identique à cpu
            #Alors écrire "Egalité."
        
        #Sinon si playerChoice égal à 0
            #Si cpuChoice égal à 2
                #Alors écrire "Manche gagnée."
                #Incrémenter scorePlayer de 1
            #Sinon 
                #Ecrire "Manche perdue."
                #Incrémenter à scoreCpu de 1
        
        #Sinon si playerChoice égal à 1
            #Si cpuChoice égal 2
                #Alors écrire "Manche gagnée." 
                #Incrémenter scorePlayer de 1
            #Sinon 
                #Ecrire "Manche perdue."
                #Incrémenter scoreCpu de 1
        
        #Sinon si playerChoice égal à 2
            #Si cpuChoice égal à 1
                #Alors écrire "Manche gagnée."
                #Incrémenter scorePlayer de 1
            #Sinon 
                #Ecrire "Manche perdue."
                #Incrémenter scoreCpu de 1
        
        #Sinon playerChoice ne renvoi à aucun index de game
            #Ecrire "Choix impossible!"
        
        #Si scorePlayer égal à 2:
            #Ecrire scorePlayer"/"scoreCpu ". Vous avez gagné."
            #Assigner scoreCpu à la valeur 0
            #Assigner scorePlayer à la valeur 0
        
        #Sinon scoreCPU égal à 2:
            #Ecrire scoreCpu"/"scorePlayer ". Vous avez perdu."
            #Assigner scoreCpu à la valeur 0
            #Assigner scorePlayer à la valeur
        
        #Retourner


#Executer la fonction pierreFeuilleCiseaux



#FIN












    #Tant que le joueur et le cpu ont un choix identique
        #Ecrire "Egalité!"
        #Redéfinir une variable cpu qui choisira aléatoirement pierre, feuille ou ciseau à partir du tableau game
    #Sinon si cpu et player ont des choix différents 
        #