def jeuImperatif(choice):
    answer = input("La lettre à deviner :")
    n = 0
    while choice != answer:
        answer = input("Devine la lettre à nouveau :")
        n = n + 1
    return f"Bien joué! Ça a pris {n} essais"

def jeuRecursif(lettre):
    if lettre == input("Lettre que tu dois deviner :"):
        return 1
    return jeuRecursif(lettre) + 1

#print(jeuImperatif("m"))
print(jeuRecursif("m"))