
# Nombre de matières
nombre_matieres = int(input("Combien de matières avez-vous ? "))

# Création des listes
matieres = []
notes = []
coefficients_ue1 = []
coefficients_ue2 = []
coefficients_ue3 = []

# Saisie des matières, notes et coefficients
for i in range(nombre_matieres):

    matiere = input("Nom de la matière : ")
    note = float(input("Moyenne : "))

    coef1 = float(input("Coefficient UE1 : "))
    coef2 = float(input("Coefficient UE2 : "))
    coef3 = float(input("Coefficient UE3 : "))

    matieres.append(matiere)
    notes.append(note)

    coefficients_ue1.append(coef1)
    coefficients_ue2.append(coef2)
    coefficients_ue3.append(coef3)

# Initialisation des sommes
somme_ue1 = 0
somme_ue2 = 0
somme_ue3 = 0

total_coef_ue1 = 0
total_coef_ue2 = 0
total_coef_ue3 = 0

# Calcul des moyennes
for i in range(nombre_matieres):

    somme_ue1 += notes[i] * coefficients_ue1[i]
    total_coef_ue1 += coefficients_ue1[i]

    somme_ue2 += notes[i] * coefficients_ue2[i]
    total_coef_ue2 += coefficients_ue2[i]

    somme_ue3 += notes[i] * coefficients_ue3[i]
    total_coef_ue3 += coefficients_ue3[i]

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
