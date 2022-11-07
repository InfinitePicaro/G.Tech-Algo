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
def divide (x,y):
    return x / y
#5 : modulo (x,y)
def modulo (x,y):
    return x % y

#6 : salaireNet (brut, coefficient)
def salaireNet(brut, coefficient):
    return brut - (brut*coefficient)

#7 : salaireParSeconde (salaire horaire, heures par jour ouvré, nb jours ouvrés par an)
def salaireParSeconde(salaireHoraire, heuresParJourOuvré, nbJoursOuvrésParAn):
    return nbJoursOuvrésParAn * salaireHoraire * (heuresParJourOuvré/3600)