# ce fichier doit être sauvegardé dans le même répertoire que TPTaquin.py
# sinon l'importation ne fonctionnera pas

import TPTaquin

from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()



def numero(n): # n est un entier
    if n == 0 :
        resu = ''
    else :
        resu = str(n)
    return resu

def couleur(n) : #n est un entier
    if n == 0:
        resu = "black"
    elif n%2 == 1 :
        resu = "red"
    else :
        resu = "white"
    return resu


class Monbouton(Button):
    def __init__(self, fenetre,  i, j, **kwargs):
        Button.__init__(self, fenetre,command = self.clic, font = ('Times', '24', 'bold'),**kwargs)
        self.ligne = i
        self.colonne = j
    def clic(self):
        i = self.ligne
        j = self.colonne
        print(i)
        print(j)
        if i == TPTaquin.ligne_case_vide-1 and j == TPTaquin.colonne_case_vide:
            TPTaquin.haut()
            refresh()
        if i == TPTaquin.ligne_case_vide+1 and j == TPTaquin.colonne_case_vide:
            TPTaquin.bas()
            refresh()
        if i == TPTaquin.ligne_case_vide and j == TPTaquin.colonne_case_vide-1:
            TPTaquin.gauche()
            refresh()
        if i == TPTaquin.ligne_case_vide and j == TPTaquin.colonne_case_vide+1:
            TPTaquin.droite()
            refresh()





taquin = [[Monbouton(fenetre, ligne, colonne, text= numero(TPTaquin.tab[ligne][colonne]), width= 5,
                  height = 2,   borderwidth=1, bg = couleur(TPTaquin.tab[ligne][colonne]))
           for colonne in range(TPTaquin.taille)] for  ligne in range(TPTaquin.taille)]

for ligne in range(TPTaquin.taille):
        for colonne in range(TPTaquin.taille):
            taquin[ligne][colonne].grid(row=ligne, column=colonne)



def fin_de_partie():
    if askyesno('Vous avez gagné', 'Voulez-vous rejouer ?'):
        TPTaquin.melange()
        refresh()
    else :
        print('FIN')
        fenetre.destroy()

def refresh():
    for ligne in range(TPTaquin.taille):
        for colonne in range(TPTaquin.taille):
            taquin[ligne][colonne]["text"] = numero(TPTaquin.tab[ligne][colonne])
            taquin[ligne][colonne]["bg"] = couleur(TPTaquin.tab[ligne][colonne])
    if TPTaquin.gameover():
        fin_de_partie()


def clavier(event):
    touche = event.keysym
    print(touche)
    if touche == "Up" :
        TPTaquin.bas()
        refresh()

    if touche == "Down" :
        TPTaquin.haut()
        refresh()

    if touche == "Left" :
        TPTaquin.droite()
        refresh()

    if touche == "Right" :
        TPTaquin.gauche()
        refresh()



fenetre.focus_set()
fenetre.bind("<Key>", clavier)


fenetre.mainloop()
