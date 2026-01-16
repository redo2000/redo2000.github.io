"""
Programme pour compléter le tableau des matériaux photoélectriques
Utilise les relations: E = h*f = h*c/λ et W = h*f_seuil
"""

# Constantes physiques
h = 6.626e-34  # Constante de Planck (J.s)
c = 3e8        # Vitesse de la lumière (m/s)

# Données des matériaux
materiaux = {
    'a. Argent (Ag)': {
        'lambda_seuil': 0.27e-6,  # en mètres
    },
    'b. Platine (Pt)': {
        'f_seuil': 4.5e14,  # en Hz
    },
    'c. Césium (Cs)': {
        'lambda_seuil': 0.19e-6,  # en mètres
    },
    'd. Calcium (Ca)': {
        'f_seuil': 6.7e14,  # en Hz
    }
}

print("="*70)
print("CALCUL DES VALEURS MANQUANTES POUR L'EFFET PHOTOÉLECTRIQUE")
print("="*70)

# Calculs pour chaque matériau
for nom, donnees in materiaux.items():
    print(f"\n{nom}")
    print("-" * 50)

    # Si on a la longueur d'onde seuil
    if 'lambda_seuil' in donnees:
        lambda_seuil = donnees['lambda_seuil']
        # Calculer la fréquence seuil: f = c/λ
        f_seuil = c / lambda_seuil
        # Calculer le travail d'extraction: W = h*f
        W = h * f_seuil

        print(f"  Longueur d'onde seuil: {lambda_seuil*1e6:.2f} μm")
        print(f"  Fréquence seuil: {f_seuil:.2e} Hz")
        print(f"  Travail d'extraction: {W:.2e} J")
        print(f"  Travail d'extraction: {W/1.6e-19:.2f} eV")

    # Si on a la fréquence seuil
    elif 'f_seuil' in donnees:
        f_seuil = donnees['f_seuil']
        # Calculer la longueur d'onde seuil: λ = c/f
        lambda_seuil = c / f_seuil
        # Calculer le travail d'extraction: W = h*f
        W = h * f_seuil

        print(f"  Fréquence seuil: {f_seuil:.2e} Hz")
        print(f"  Longueur d'onde seuil: {lambda_seuil*1e6:.2f} μm")
        print(f"  Travail d'extraction: {W:.2e} J")
        print(f"  Travail d'extraction: {W/1.6e-19:.2f} eV")

print("\n" + "="*70)
print("TABLEAU COMPLÉTÉ")
print("="*70)
print(f"{'Matériau':<20} {'Fréquence seuil':<20} {'Longueur d_onde':<20} {'Travail (eV)'}")
print("-" * 70)

# Affichage du tableau complété
for nom, donnees in materiaux.items():
    if 'lambda_seuil' in donnees:
        lambda_seuil = donnees['lambda_seuil']
        f_seuil = c / lambda_seuil
    else:
        f_seuil = donnees['f_seuil']
        lambda_seuil = c / f_seuil

    W_eV = (h * f_seuil) / 1.6e-19

    print(f"{nom:<20} {f_seuil:.2e} Hz     {lambda_seuil*1e6:.2f} μm           {W_eV:.2f}")

print("="*70)