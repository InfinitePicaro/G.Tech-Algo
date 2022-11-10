###BO 1

#DEBUT

#Définir une fonction pierreFeuilleCiseaux qui permet au joueur de faire son choix
    #Ecrire les règles du jeu
    #Créer un tableau game = ["pierre","feuille","ciseaux"]
    #Créer un input player qui détermine le choix du joueur parmis un index de game
    #Ecrire "Vous avez choisi {input(player)}"
    #Créer une variable cpu qui choisira aléatoirement pierre, feuille ou ciseau à partir du tableau game
    #Si player a un choix identique à cpu
        #Alors écrire "Egalité!"
    #Sinon si player choisi game[0]
        #Si cpu choisi game[2]
            #Alors écrire "Vous avez gagner!"
        #Sinon 
            #Ecrire "Vous avez Perdu!"
    #Sinon si player choisi game[1]
        #Si cpu choisi game[0]
            #Alors écrire "Vous avez gagner!"
        #Sinon 
            #Ecrire "Vous avez Perdu!"
    #Sinon si player choisi game[2]
        #Si cpu choisi game[1]
            #Alors écrire "Vous avez gagner!"
        #Sinon 
            #Ecrire "Vous avez Perdu!"
    #Sinon le choix du player est incorrect
        #Ecrire "Choix inorrect!"


#FIN












    #Tant que le joueur et le cpu ont un choix identique
        #Ecrire "Egalité!"
        #Redéfinir une variable cpu qui choisira aléatoirement pierre, feuille ou ciseau à partir du tableau game
    #Sinon si cpu et player ont des choix différents 
        #