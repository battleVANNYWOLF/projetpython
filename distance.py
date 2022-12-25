import math
Xa = float(input("Veuillez saisir la coordonnee de X de A:"))
Xb = float(input("Veuillez saisir la coordonnee de X de B:"))
Ya = float(input("Veuillez saisir la coordonne de Y de A:"))
Yb = float(input("Veuillez saisir la coordonne de Y de B:"))
AB = (Xb - Xa)**2 + (Yb - Ya)**2
AB = math.sqrt(AB)
print("La distance entre les points A et B est :", format(AB,".2f"))