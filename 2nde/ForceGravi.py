# Calcul de la force de gravitation
G = 6.67e-11
mA = float(input("Donner la valeur de la masse en kg, mA = "))
mB = float(input("Donner la valeur de la masse en kg, mB = "))
d = float(input("Donner la distance (en m) entre A et B d = "))
F = G * mA * mB / d ** 2
print("L'intensité de la force F est :",f"{F:.2e}",  "N")