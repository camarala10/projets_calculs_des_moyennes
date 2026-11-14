from tkinter import *
from tkinter import ttk
fen = Tk()
fen.geometry('400x400')
fen.title('le nom de ma fenetre')
#fen.resizable(height=False,width=False)
fen['bg']='black'

cadre = ttk.Frame(fen)
cadre.grid()

texte1 = ttk.Label(cadre,text='premiere valeur')
texte1.grid(column=0,row=0,padx=50,pady=50) 
'''#une autre facon de faire une zone de texte
zone = Label(cadre, text='bonjour')
zone.grid()'''
saisie1 = ttk.Entry(cadre)
saisie1.grid(column=1,row=0)

texte2 = ttk.Label(cadre,text='deuxieme texte')
texte2.grid(column=0,row=1,padx=50,pady=50)
saisie2=ttk.Entry(cadre)
saisie2.grid(column=1,row=1)

texte4=ttk.Label(cadre,text='quatrieme texte')
texte4.grid(column=0,row=3,padx=50,pady=50)
saisie4=ttk.Entry(cadre)
saisie4.grid(column=1,row=3)

texte3=ttk.Label(cadre,text='troisieme texte')
texte3.grid(column=0,row=2,padx=50,pady=50)
saisie3=ttk.Entry(cadre)
saisie3.grid(column=1,row=2)

def calcul():
    somme = float(saisie1.get())+float(saisie2.get())+float(saisie3.get())+float(saisie4.get())
    print('la somme des quatre nombre est :',somme)
    quotient= (float(saisie1.get())+float(saisie2.get())+float(saisie3.get())+float(saisie4.get()))/4
    print('le quotient est :',quotient)
    texte5=ttk.Label(cadre,text= 'la somme des quatre nombre est :' + str(somme) + 'et leur quotient est :' + str(quotient))
    texte5.grid(column=2,row=4)

bouton = ttk.Button(cadre,text='calculer',command=calcul)
bouton.grid(column=2,row=3,padx=50,pady=50)
quitter= ttk.Button(cadre,text='quitter',command = fen.destroy)
quitter.grid(column=0,row=4)
fen.mainloop()