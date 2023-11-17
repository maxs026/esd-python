EXERCICES PYTHON :

def multiplie(a, b):
    resultat = 0
    while b > 0:
        resultat += a
        b -= 1
    return resultat

def puissance(base, exposant):
  
    resultat = 1
    while exposant > 0:
        resultat = multiplie(resultat, base)
        exposant -= 1
    return resultat

Exemples d'utilisation : 
resultat_multiplication = multiplie(5, 3)
resultat_puissance = puissance(2, 4)
