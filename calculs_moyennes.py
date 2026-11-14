
from tkinter import *
from tkinter import ttk
import numpy as np

# Création de la fenêtre
fen = Tk()
fen.title("Résultats du premier semestre")
fen.geometry("700x750")

frm = ttk.Frame(fen)
frm.grid()

titre = ttk.Label(frm, text="Saisie des notes")
titre.grid(column=1, row=0, padx=20, pady=20)

# Liste des matières
matieres = [f"R{i}" for i in range(101, 116)] + [f"SAE{i}" for i in range(11, 17)]

# Coefficients des trois UE
coef1 = [10,10,7,7,0,5,0,6,0,5,4,2,5,5,0,20,20,0,0,0,7]

coef2 = [4,0,2,8,6,0,0,0,0,5,5,2,9,9,3,0,0,29,0,0,7]

coef3 = [4,0,2,0,0,5,15,6,4,5,5,2,0,0,3,0,0,0,20,20,7]

# Création des zones de saisie
saisies = []

for i, matiere in enumerate(matieres):

    mat = ttk.Label(frm, text=matiere)
    mat.grid(column=0, row=i+1, padx=20, pady=3)

    saisie = ttk.Entry(frm)
    saisie.grid(column=1, row=i+1)

    saisies.append(saisie)


# Fonction de calcul
def calcul():

    notes = []

    for saisie in saisies:
        notes.append(float(saisie.get()))

    moy1 = round(np.average(notes, weights=coef1), 2)
    moy2 = round(np.average(notes, weights=coef2), 2)
    moy3 = round(np.average(notes, weights=coef3), 2)

    resultat1.config(text=f"La moyenne de l'UE1 est : {moy1}")
    resultat2.config(text=f"La moyenne de l'UE2 est : {moy2}")
    resultat3.config(text=f"La moyenne de l'UE3 est : {moy3}")


# Affichage des résultats
resultat1 = ttk.Label(frm, text="")
resultat1.grid(column=0, row=23, padx=20, pady=5)

resultat2 = ttk.Label(frm, text="")
resultat2.grid(column=0, row=24, padx=20, pady=5)

resultat3 = ttk.Label(frm, text="")
resultat3.grid(column=0, row=25, padx=20, pady=5)


# Bouton Valider
btn1 = ttk.Button(frm, text="Valider", command=calcul)
btn1.grid(column=0, row=22, pady=10)

# Bouton Quitter
btn2 = ttk.Button(frm, text="Quitter", command=fen.destroy)
btn2.grid(column=1, row=22, pady=10)

fen.mainloop()
