###BO 1


#DEBUT

#On admet la fonction input()
#On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe

#Définir une fonction pierreFeuilleCiseaux qui lance une partie
    #Ecrire les règles du jeu
    #Créer un tableau game = ["pierre","feuille","ciseaux"]
    #Initiliser une variable scorePlayer
    #Initialiser une variable scoreCpu
    #Définir la variable playerChoice avec comme valeur le retour de la fonction input("Choisis ce que tu veux faire : 0 pour pierre, 1 pour feuille, 2 pour ciseaux :")
    #Ecrire "Vous avez choisi {playerChoice}"
    #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction random()
    #Tant que scorePlayer inférieur à 2 ou scoreCpu inférieur à 2:
        
        #Si player a un choix identique à cpu
            #Alors écrire "Egalité!"
        
        #Sinon si player égal à 0
            #Si cpu égal à 2
                #Alors écrire "Manche gagnée."
                #Ajouter +1 à scorePlayer
            #Sinon 
                #Ecrire "Vous avez Perdu!"
                #Ajouter +1 à scoreCpu
        
        #Sinon si player égal à 1
            #Si cpu égal 2
                #Alors écrire "Manche gagnée." 
                #Ajouter +1 à scorePlayer
            #Sinon 
                #Ecrire "Vous avez Perdu!"
                #Ajouter +1 à scoreCpu
        
        #Sinon si player égal à 2
            #Si cpu égal à 1
                #Alors écrire "Manche gagnée."
                #Ajouter +1 à scorePlayer
            #Sinon 
                #Ecrire "Vous avez Perdu!"
                #Ajouter +1 à scoreCpu
        
        #Sinon le choix du player est incorrect
            #Ecrire "Choix impossible!"
        
        #Si scorePlayer égal à 2:
            #Ecrire "{playerScore}/{cpuScore}. Vous avez gagné."
            #réinitialiser scoreCpu
            #réinitialiser scorePlayer
        
        #Sinon scoreCPU égal à 2:
            #Ecrire "{cpuScore}/{playerScore}. Vous avez perdu."
            #réinitialiser scoreCpu
            #réinitialiser scorePlayer
        
        #Retourner



#FIN












    #Tant que le joueur et le cpu ont un choix identique
        #Ecrire "Egalité!"
        #Redéfinir une variable cpu qui choisira aléatoirement pierre, feuille ou ciseau à partir du tableau game
    #Sinon si cpu et player ont des choix différents 
        #