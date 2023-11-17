def multiplie(a, b):

    Multiplie deux nombres en utilisant des additions successives.
    
    resultat = 0
    while b > 0:
        resultat += a
        b -= 1
    return resultat

def puissance(base, exposant):
    
    Calcule la puissance d'un nombre par multiplication successive.
    
    resultat = 1
    while exposant > 0:
        resultat = multiplie(resultat, base)
        exposant -= 1
    return resultat

Exemples d'utilisation :

resultat_multiplication = multiplie(5, 3)
resultat_puissance = puissance(2, 4)

print(f"Résultat de la multiplication : {resultat_multiplication}")
print(f"Résultat de la puissance : {resultat_puissance}")
