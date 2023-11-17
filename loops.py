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




exercice : Somme des Nombres 

def somme_des_nombres():
  
    Calcule et affiche la somme des nombres de 1 à N, où N est saisi par l'utilisateur.
    
    try:
        Demander à l'utilisateur de saisir un nombre entier
        N = int(input("Veuillez saisir un nombre entier N : "))
        
        Vérifier que N est positif
        if N < 0:
            print("Veuillez saisir un nombre entier positif.")
            return

        Calculer la somme des nombres de 1 à N avec une boucle for
        somme = 0
        for i in range(1, N + 1):
            somme += i

        Afficher le résultat
        print(f"La somme des nombres de 1 à {N} est : {somme}")

    except ValueError:
        print("Veuillez saisir un nombre entier valide.")

Appeler la fonction
somme_des_nombres()

exercice : Table de multiplication

def table_de_multiplication():
    
    Affiche la table de multiplication d'un nombre N de 1 à 10.
    
    try:
        Demander à l'utilisateur de saisir un nombre entier
        N = int(input("Veuillez saisir un nombre entier N : "))
        
        Afficher la table de multiplication de 1 à 10
        print(f"Table de multiplication de {N} :")
        for i in range(1, 11):
            resultat = N * i
            print(f"{N} x {i} = {resultat}")

    except ValueError:
        print("Veuillez saisir un nombre entier valide.")

Appeler la fonction
table_de_multiplication()



exercice : pair ou impair 

def pair_ou_impair():

Affiche les nombres de 1 à 10 et indique si chaque nombre est pair ou impair.
    
    print("Nombres de 1 à 10 et leur parité :")
    for nombre in range(1, 11):
        if nombre % 2 == 0:
            print(f"{nombre} est pair.")
        else:
            print(f"{nombre} est impair.")

Appeler la fonction
pair_ou_impair()
