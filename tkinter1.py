from tkinter import * # importation de toutes les fonctions tkinter 
fenetre = Tk() # creation de la fenetre
fenetre.geometry('400x400') # pour regler la dimension de ma fenetre
fenetre.title('le titre de ma fenetre')
fenetre ['bg']='black' # le couleur du fond de la page
fenetre.resizable(height=False, width=False) # pour qu'on ne puisse pas arriver a modifier votre fenetre d'agrandir ou de modifier 
label = Label(fenetre, text="bonjour suis un etudiant") #  est un zone de texte 
label.pack() # permettra d'afficher votre label oubien on pouvait utiliser label.place(x='20',y='30')
def bonjour (): 
    print("merci d'avoir cliquer sur le bouton") #la phrase qui sera afficher sur ton  terminal le nombre de fois que tu cliquerasur le bonton
#et avec command il faudra d'abord definir la fonction bonjour ave=ant d'utiliser command
bouton = Button(fenetre,text='veuillez cliquer',bg = 'purple',fg = 'orange',command =bonjour) # le bouton le nom de ls fenetre puis le text et ensuite bg pour le fond fg pour la couler 
bouton.pack()
ma_var = str()
entre = Entry(fenetre,text= ma_var)
entre.pack()


fenetre.mainloop() # permet de lancer notre fenetre et au moment ou on ferme notre fenetre pour le boucle puisse s'arreter 
