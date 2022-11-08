#DEBUT EXO1 Partie 1
r = 12000
s = 1250
e = 10
rh = 230
assertionFinale = (( (365 * 3) / (24 - (16 - 8)) ) * (rh) > r) == (e * s < r) 

assertionUn = (( (365 * 3) / (24 - (16 - 8)) ) * (rh) > r) #True
assertionDeux = (e * s < r)  #False

assertionFinale = assertionUn == assertionDeux #False
#FIN EXO1 Partie 1



#DEBUT EXO1 Partie 2
r = 12000
s = 1250
e = 10
rh = 230
assertionFinale = (( (365 * 3) / (4 - (12 - 8)) ) * (rh) > r) == (e * s < r) 

assertionUn = (( (365 * 3) / (4 - (12 - 8)) ) * (rh) > r) #False
assertionDeux = (e * s < r) #False

assertionFinale = (( (365 * 3) / (4 - (12 - 8)) ) * (rh) > r) == (e * s < r)  #True
#FIN EXO1 Partie 2



#EXOS 

#DEBUT


#1 : add (x,y)
def add (x,y):
    return x + y

#2 : sub (x,y)
def sub (x,y):
    return x - y

#3 : multiply (x,y)
def multiply (x,y):
    return x * y

#4 : divide (x,y)

#Définir une fonction qui divise x par y et retourne le résultat
def divide (x,y):
    #Si Y est égal à 0
    if y == 0:
        #Alors écrire message d'erreur
        print ("La matière grise, ça s'utilise hein.")
        #Retourner vide
        return 
    #Sinon
    else:
        #Alors retourner le résultat 
        return x / y

#5 : modulo (x,y)
def modulo (x,y):
    return x % y

#6 : salaireNet (brut, coefficient)
def salaireNet(brut, coefficient):
    return brut - (brut * coefficient)

#7 : salaireParSeconde (salaire horaire, heures par jour ouvré, nb jours ouvrés par an)
def salaireParSeconde(salaireHoraire, heuresParJourOuvré, nbJoursOuvrésParAn):
    #Calculer mon salaire annuel
    salaireAnnuel = nbJoursOuvrésParAn * heuresParJourOuvré * salaireHoraire
    #Calculer le nombre de secondes dans une année
    nbSecondesParAn = 365 * 24 * 60 * 60
    #Je pose et retourne la division
    return salaireAnnuel / nbSecondesParAn


#7 Fin   

#Définir une fonction withdrawFees qui retire un % d'un total en fonction du salaire total et d'un %
def withdrawFees(total, percent):
    #Définir fees en fonction d'un total et d'un %
    fees = total * (percent/100)
    #Soustraire fees au total
    result = total - fees
    #retourner la valeur obtenue
    return result

#Définir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur publique
    if isPublic:
        #Alors je soustrais 15% de mon salaire Brut à mon salaire brut et je l'assigne à la variable salaire
        #salaireNet = salaireBrut - (salaireBrut * 15/100)
        salaireNet = withdrawFees(salaireBrut, 15)
    #Sinon je suis un travailleur du secteur privé
    else:
        #Alors je soustrais 23% de mon salaire brut à mon salaire brut et je l'assigne à la variable salaire (je douille sa race)
        #salaireNet = salaireBrut - (salaireBrut * 23/100)
        salaireNet = withdrawFees(salaireBrut, 23)
    
    
    #Retourner salaireNet
    return salaireNet



#Exercice :
#   Faire un mini-jeu qui affiche un message lorsque input renvoie le bon caractère
#   Le caractère doit être paramètrable



#DEBUT
def input(): 
    return


#Définir une fonction qui prend en argument un caractère de type string
def jeuImperatif(choice):
    #Définir une variable réponse avec comme valeur un caractère aléatoire de type string donnée par def input
    answer = input()
    #Définir une variable d'un compteur de nouvel essai commençant à 0
    compteur = 0
    #Tant que le caractère choisi est différent de réponse
    while choice != answer:
        #Redéfinir la valeur de réponse avec input
        answer = input()
        #Ajouter 1 au compteur de nouvel essai
        compteur = compteur + 1
    #Renvoyer réponse
    return f"Bien joué! Ça a pris {compteur} essais"
    #Ecrire le message "Victore!""

#Définir une fonction qui prend en argument un caractère de type string le compteur n à 0
def jeuRecursif(lettre, n = 0):
    #Si le caractère de type string choisi n'est pas le même qu'un choix aléatoire
    if lettre == input():
        #Alors renvoyer n
        return n
    #Renvoyer la lettre et le nombre d'essai
    return jeuRecursif(lettre, n + 1)


def jeuRecursifV2(lettre):
    if lettre == input():
        return 1
    return jeuRecursifV2(lettre) + 1

#FIN

#EXO1
#Renvoyer/Afficher un message

#EXO2
#Faire une fonction qui itère sur tous les index d'un tableau renvoyant une chaîne de caractère
#avec l'ensemble des occurences d'un chiffre e.g.:
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) doit renvoyer "0, 4, 7"







#FIN

