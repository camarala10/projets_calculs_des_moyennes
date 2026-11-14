
# Nombre de matières
nombre_matieres = int(input("Combien de matières avez-vous ? "))

# Initialisation des sommes pour UE1
somme_notes_ue1 = 0
somme_coef_ue1 = 0
# Initialisation des sommes pour UE2
somme_notes_ue2 = 0
somme_coef_ue2 = 0
# Initialisation des sommes pour UE3
somme_notes_ue3 = 0
somme_coef_ue3 = 0
# Boucle de saisie
for i in range(nombre_matieres):

    nom_matiere = input("Nom de la matière : ")

    note = float(input(f"Moyenne de {nom_matiere} : "))
    coef1 = float(input(f"Coefficient UE1 de {nom_matiere} : "))
    coef2 = float(input(f"Coefficient UE2 de {nom_matiere} : "))
    coef3 = float(input(f"Coefficient UE3 de {nom_matiere} : "))

    # Calcul UE1
    somme_notes_ue1 += note * coef1
    somme_coef_ue1 += coef1

    # Calcul UE2
    somme_notes_ue2 += note * coef2
    somme_coef_ue2 += coef2

    # Calcul UE3
    somme_notes_ue3 += note * coef3
    somme_coef_ue3 += coef3

# Calcul des moyennes
if somme_coef_ue1 > 0 and somme_coef_ue2 > 0 and somme_coef_ue3 > 0:

    moyenne_ue1 = somme_notes_ue1 / somme_coef_ue1
    moyenne_ue2 = somme_notes_ue2  / somme_coef_ue2
    moyenne_ue3 = somme_notes_ue3   / somme_coef_ue3

    print("Moyenne UE1 :", round(moyenne_ue1, 2))
    print("Moyenne UE2 :", round(moyenne_ue2, 2))
    print("Moyenne UE3 :", round(moyenne_ue3, 2))

else:
    print("Erreur : un coefficient total est nul.")
