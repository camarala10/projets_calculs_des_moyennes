
import numpy as np
import matplotlib.pyplot as plt

# Création de la liste des matières
matiere = [f"R{i}" for i in range(101, 116)] + [f"SAE{i}" for i in range(11, 17)]

# Listes des coefficients des trois UE
list_coef1 = [10, 10, 7, 7, 0, 5, 0, 6, 0, 5, 4, 2, 5, 5, 0, 20, 20, 0, 0, 0, 7]
list_coef2 = [4, 0, 2, 8, 6, 0, 0, 0, 0, 5, 5, 2, 9, 9, 3, 0, 0, 29, 0, 0, 7]
list_coef3 = [4, 0, 2, 0, 0, 5, 15, 6, 4, 5, 5, 2, 0, 0, 3, 0, 0, 0, 20, 20, 7]

# Saisie des notes
list_notes = [float(input(f"Quelle est la note pour {element} ? ")) for element in matiere]

# Calcul des moyennes
def calcul_moy(list_coef):
    return round(np.average(list_notes, weights=list_coef), 3)

moy1 = calcul_moy(list_coef1)
moy2 = calcul_moy(list_coef2)
moy3 = calcul_moy(list_coef3)

print("Moyenne UE1 :", moy1)
print("Moyenne UE2 :", moy2)
print("Moyenne UE3 :", moy3)

# Attribution des couleurs
def couleur(moy):
    if moy >= 10:
        return "green"
    elif 8 <= moy < 10:
        return "orange"
    else:
        return "red"

couleurs = [couleur(moy1), couleur(moy2), couleur(moy3)]

# Construction du graphique
plt.bar(["UE1", "UE2", "UE3"], [moy1, moy2, moy3], color=couleurs, label="Moyennes")

# Documentation du graphique
plt.title("Moyennes des trois UE - Semestre 1")
plt.xlabel("Unités d'enseignement")
plt.ylabel("Moyennes sur 20")
plt.ylim(0, 20)
plt.legend()
plt.grid(axis="y")

plt.show()

# Commentaire sur la décision du jury
print("Les résultats affichés concernent uniquement le semestre 1.")
print("La décision définitive du jury sera déterminée avec les moyennes annuelles.")
