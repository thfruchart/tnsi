# TP Taquin A COMPLETER sans interface graphique
# la plupart des fonctions seront à compléter dans le TP
# ATTENTION : ne pas changer le nom des fonctions !
# sinon, l'interface graphique ne pourra pas fonctionner

from random import randint

taille = 3 # cette variable est utilisée dans la partie graphique

# tableau ordonné :
objectif = [[1,2,3],   
            [4,5,6],
            [7,8,0]]


# tableau mélangé à remettre dans l'ordre en utilisant les fonctions définies plus bas :
# haut() bas() gauche() et droite()
tab = [[2, 6, 3],
       [7, 0, 5],
       [4, 1, 8]]

# le 0 représente la case vide, qui permet aux autres cases de se déplacer
# dans le tableau ci-dessus, le zéro est initialement en: ligne 1 colonne 1
ligne_case_vide = 1
colonne_case_vide = 1
# ces valeurs seront à actualiser au cours du jeu



def affiche():
    for i in range(taille):
        print(tab[i])


def haut():
    """ cette procédure déplace la case vide vers le haut (si c'est possible)
    c'est à dire que le numéro situé une ligne au dessus du 0 va descendre
    et que le 0 va monter"""
    global ligne_case_vide
    


def bas():
    """ cette procédure déplace la case vide vers le bas (si c'est possible)
    c'est à dire que le numéro situé une ligne en dessous du 0 va monter
    et que le 0 va descendre"""
    global ligne_case_vide
    tab[ligne_case_vide][colonne_case_vide] = tab[ligne_case_vide+1][colonne_case_vide]
    tab[ligne_case_vide+1][colonne_case_vide] = 0
    ligne_case_vide = ligne_case_vide+1
    


def gauche():
    """ cette procédure déplace la case vide vers la gauche (si c'est possible)
    c'est à dire que le numéro situé une colonne à gauche du 0 va
    se déplacer vers la droite, et que le 0 va se déplacer à gauche"""   
    global colonne_case_vide



def droite():
    """ cette procédure déplace la case vide vers la droite (si c'est possible)
    c'est à dire que le numéro situé une colonne à droite du 0 va
    se déplacer vers la gauche, et que le 0 va se déplacer à droite"""
    global colonne_case_vide


def gameover():
    #cette fonction doit tester si le tableau est remis dans l'état initial
    # c'est à dire : 123
    #                456
    #                780
    return False

def melange():
    return None 
