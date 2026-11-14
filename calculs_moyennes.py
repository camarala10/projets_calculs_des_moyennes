
# Nombre de matières
nombre_matieres = int(input("Combien de matières avez-vous ? "))

# Création des dictionnaires
notes = {}
coefficients_ue1 = {}
coefficients_ue2 = {}
coefficients_ue3 = {}

# Saisie des matières, notes et coefficients
for i in range(nombre_matieres):

    matiere = input("Nom de la matière : ")
    note = float(input("Moyenne : "))

    coef1 = float(input("Coefficient UE1 : "))
    coef2 = float(input("Coefficient UE2 : "))
    coef3 = float(input("Coefficient UE3 : "))

    # Ajout des informations dans les dictionnaires
    notes[matiere] = note
    coefficients_ue1[matiere] = coef1
    coefficients_ue2[matiere] = coef2
    coefficients_ue3[matiere] = coef3

# Initialisation des sommes
somme_ue1 = 0
somme_ue2 = 0
somme_ue3 = 0

total_coef_ue1 = 0
total_coef_ue2 = 0
total_coef_ue3 = 0

# Calcul des moyennes
for matiere in notes:

    somme_ue1 += notes[matiere] * coefficients_ue1[matiere]
    total_coef_ue1 += coefficients_ue1[matiere]

    somme_ue2 += notes[matiere] * coefficients_ue2[matiere]
    total_coef_ue2 += coefficients_ue2[matiere]

    somme_ue3 += notes[matiere] * coefficients_ue3[matiere]
    total_coef_ue3 += coefficients_ue3[matiere]

# Affichage des résultats
if total_coef_ue1 > 0:
    moyenne_ue1 = somme_ue1 / total_coef_ue1
    print("Moyenne UE1 :", round(moyenne_ue1, 2))
else:
    print("Aucun coefficient pour UE1")

if total_coef_ue2 > 0:
    moyenne_ue2 = somme_ue2 / total_coef_ue2
    print("Moyenne UE2 :", round(moyenne_ue2, 2))
else:
    print("Aucun coefficient pour UE2")

if total_coef_ue3 > 0:
    moyenne_ue3 = somme_ue3 / total_coef_ue3
    print("Moyenne UE3 :", round(moyenne_ue3, 2))
else:
    print("Aucun coefficient pour UE3")
