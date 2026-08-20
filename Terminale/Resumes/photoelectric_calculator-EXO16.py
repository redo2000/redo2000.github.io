"""
Calculateur interactif pour l'effet photoélectrique
Calcule les paramètres manquants à partir de la longueur d'onde ou de la fréquence
"""

# Constantes physiques
h = 6.626e-34  # Constante de Planck (J.s)
c = 3e8        # Vitesse de la lumière (m/s)
eV = 1.602e-19   # Conversion Joules vers électronvolts

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*60)
    print("   CALCULATEUR EFFET PHOTOÉLECTRIQUE")
    print("="*60)
    print("\nQue souhaitez-vous entrer comme donnée ?")
    print("\n  [L] - Longueur d'onde seuil (en μm)")
    print("  [F] - Fréquence seuil (en Hz)")
    print("  [Q] - Quitter le programme")
    print("\n" + "-"*60)

def calculer_depuis_longueur_onde(lambda_um):
    """
    Calcule la fréquence et le travail d'extraction à partir de la longueur d'onde

    Args:
        lambda_um: longueur d'onde en micromètres
    """
    # Conversion en mètres
    lambda_m = lambda_um * 1e-6

    # Calcul de la fréquence seuil: f = c/λ
    f_seuil = c / lambda_m

    # Calcul du travail d'extraction: W = h*f
    W_joules = h * f_seuil
    W_eV = W_joules / eV

    # Affichage des résultats
    print("\n" + "="*60)
    print("   RÉSULTATS DU CALCUL")
    print("="*60)
    print(f"\n  Donnée entrée:")
    print(f"    • Longueur d'onde seuil: {lambda_um} μm ({lambda_m} m)")
    print(f"\n  Valeurs calculées:")
    print(f"    • Fréquence seuil: {f_seuil:.4e} Hz")
    print(f"    • Travail d'extraction: {W_joules:.4e} J")
    print(f"    • Travail d'extraction: {W_eV:.3f} eV")
    print("="*60)

def calculer_depuis_frequence(f_hz):
    """
    Calcule la longueur d'onde et le travail d'extraction à partir de la fréquence

    Args:
        f_hz: fréquence en Hertz
    """
    # Calcul de la longueur d'onde seuil: λ = c/f
    lambda_m = c / f_hz
    lambda_um = lambda_m * 1e6

    # Calcul du travail d'extraction: W = h*f
    W_joules = h * f_hz
    W_eV = W_joules / eV

    # Affichage des résultats
    print("\n" + "="*60)
    print("   RÉSULTATS DU CALCUL")
    print("="*60)
    print(f"\n  Donnée entrée:")
    print(f"    • Fréquence seuil: {f_hz:.4e} Hz")
    print(f"\n  Valeurs calculées:")
    print(f"    • Longueur d'onde seuil: {lambda_um:.3f} μm ({lambda_m:.4e} m)")
    print(f"    • Travail d'extraction: {W_joules:.4e} J")
    print(f"    • Travail d'extraction: {W_eV:.3f} eV")
    print("="*60)

def obtenir_valeur(type_valeur):
    """
    Demande à l'utilisateur d'entrer une valeur avec gestion des erreurs

    Args:
        type_valeur: string décrivant le type de valeur attendue

    Returns:
        float: la valeur entrée par l'utilisateur
    """
    while True:
        try:
            print(f"\nEntrez la valeur de {type_valeur}: ", end='', flush=True)
            valeur = float(input())
            if valeur <= 0:
                print("⚠ Erreur: La valeur doit être strictement positive!")
                continue
            return valeur
        except ValueError:
            print("⚠ Erreur: Veuillez entrer un nombre valide!")
        except EOFError:
            print("\n⚠ Erreur: Entrée interrompue. Veuillez réessayer.")
            continue

def main():
    """Fonction principale du programme"""
    print("\n" + "="*60)
    print("   BIENVENUE DANS LE CALCULATEUR PHOTOÉLECTRIQUE")
    print("="*60)

    while True:
        afficher_menu()

        print("\nVotre choix (L/F/Q): ", end='', flush=True)
        choix = input().strip().upper()

        if choix in ['L', 'l']:
            # Calcul à partir de la longueur d'onde
            lambda_um = obtenir_valeur("la longueur d'onde seuil (en μm)")
            calculer_depuis_longueur_onde(lambda_um)

        elif choix in ['F', 'f']:
            # Calcul à partir de la fréquence
            f_hz = obtenir_valeur("la fréquence seuil (en Hz)")
            calculer_depuis_frequence(f_hz)

        elif choix in ['Q', 'q']:
            print("\n" + "="*60)
            print("   Merci d'avoir utilisé le calculateur!")
            print("   Au revoir!")
            print("="*60 + "\n")
            break

        else:
            print("\n⚠ Choix invalide! Veuillez entrer L, F ou Q.")

        # Demander si l'utilisateur veut faire un autre calcul
        print("\n\nVoulez-vous faire un autre calcul? (O/N): ", end='', flush=True)
        continuer = input().strip().upper()
        if continuer not in ['O', 'o', 'OUI', 'Y', 'YES']:
            print("\n" + "="*60)
            print("   Merci d'avoir utilisé le calculateur!")
            print("   Au revoir!")
            print("="*60 + "\n")
            break

# Lancement du programme
if __name__ == "__main__":
    main()