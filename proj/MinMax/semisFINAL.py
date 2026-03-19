# Créé par thfruchart, le 10/12/2024 en Python 3.7




#           SSSS    EEEEE  MMM     MMM  III    SSSS
#         SSS       EE     MMMMM MMMMM  III  SSS
#          SSSSS    EEEEE  MMM MMM MMM  III   SSSSS
#             SSS   EE     MMM  M  MMM  III      SSS
#          SSSS     EEEEE  MMM     MMM  III   SSSS



# DEUX JOUEURS S'AFFRONTENT
# JOUEUR 1 JOUE VERS LA DROITE
# JOUEUR 2 JOUE VERS LA GAUCHE

# A CHAQUE TOUR, UN JOUEUR PREND TOUS LES GRAINS D'UNE CASE
# PUIS IL LES SEME UN PAR UN DANS LES CASES VOISINES
# S'IL RESTE DES GRAINS A SEMER AU DELA DU PLATEAU... IL A PERDU
# S'IL SEME LE DERNIER GRAIN DANS UNE CASE VIDE...  IL A PERDU
# SINON LA PARTIE CONTINUE ET C'EST L'AUTRE JOUEUR QUI JOUE

























import pyxel
########
# INIT #
########
LARG = 256
HAUT = 128
pyxel.init(LARG, HAUT, title="Sowing")
pyxel.mouse(True)
NB_CASES = 7
l_case = (3*LARG) // (NB_CASES * 4)
rayon_grain = 3 - NB_CASES//10


plateau = [2]*NB_CASES
fini = False
joueur = +1 # Sud
derniere_case_jouee = None
scores = [0,0,0] # la case d'indice 0 ne servira pas
# le score d'un joueur se trouve dans la case score[joueur]


def tour_de_jeu(plateau, joueur, i):
    """modifie le plateau en faisant jouer la case d'indice i au joueur
    renvoie True si le coup est possible
    et False si le coup est perdant"""
    # prendre les grains de la case i
    grains = plateau[i]
    
    if grains == 0 :
        return False
    # débordement
    dernier_indice = i + joueur * grains
    if not(0<= dernier_indice < NB_CASES) :
        return False
    # dernière case vide
    if plateau[dernier_indice] == 0:
        return False
    # le coup est possible
    for j in range(grains):
        plateau[i + (j+1)* joueur] += 1
    plateau[i] = 0 # uniquement si le coup est possible, sinon le plateau est laissé inchangé
    return True



# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    global joueur, fini, derniere_case_jouee
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    if not fini and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
        x_coord, y_coord = pyxel.mouse_x, pyxel.mouse_y
        indice_case = (x_coord-LARG//8)//l_case
        #print(indice_case, y_coord)
        if HAUT//4 < y_coord< 3*HAUT//4 :
            fini = not tour_de_jeu(plateau, joueur,indice_case )                
            derniere_case_jouee = indice_case
            joueur *= -1
            # mise à jour des scores
            if fini :
                scores[joueur]+=1
    # remet le jeu à zéro si la partie est finie, par un clic droit de souris
    if fini and pyxel.btnr(pyxel.MOUSE_BUTTON_RIGHT):
        for i in range(NB_CASES):
            plateau[i] = 2
        fini = False
        
    


# =========================================================
# == DRAW
# =========================================================

def case(i,nb):
    """dessine la case d'indice i avec la quantité de grains : nb"""
    x_case = LARG // 8 + i * l_case
    y_case = HAUT//4
    pyxel.rect(x_case+4, y_case+4, l_case-8, HAUT//2-8,2)
    # dessin des grains
    dy_grain = (HAUT // 2 - 8 )//(nb+1)
    y_grain = HAUT//2 - (nb-1)*dy_grain//2
    for _ in range(nb):
        if derniere_case_jouee==i and fini:
            couleur = 8
        else :
            couleur = 11
        pyxel.circ(x_case + l_case//2, y_grain, rayon_grain, couleur)
        y_grain += dy_grain
        
    
    

def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # plateau 
    pyxel.rect(LARG // 8, HAUT//4, LARG//4*3, HAUT//2, 3)
    # cases
    for i in range(NB_CASES):
        case(i,plateau[i])
    # affichage des scores :
    pyxel.text(6*LARG//8, 7*HAUT//8, 'score : '+str(scores[1]), 7)
    pyxel.text(6*LARG//8, HAUT//8, 'score : '+str(scores[-1]), 7)
    # message pour le joueur
    if not fini : 
        if joueur>0:
            pyxel.text(LARG//8, 7*HAUT//8, 'Joueur 1 joue', 7)
            
            pyxel.rect(LARG//2, 7*HAUT//8, LARG//8, 3,15)
            x_tri = LARG//2+LARG//8
            y_tri = 7*HAUT//8
            pyxel.tri(x_tri, y_tri-5, x_tri, y_tri+6, x_tri+10, y_tri+1, 15)
        else : 
            pyxel.text(LARG//8, HAUT//8, 'Joueur 2 joue', 7)
            x_tri = LARG//2
            y_tri = HAUT//8
            pyxel.tri(x_tri, y_tri-5, x_tri, y_tri+6, x_tri-10, y_tri+1, 15)
            pyxel.rect(x_tri, y_tri, LARG//8, 3,15)
            
    else :
        if joueur>0:
            pyxel.text(LARG//8, 7*HAUT//8, 'Joueur 1 remporte la partie', 7)
        else : 
            pyxel.text(LARG//8, HAUT//8, 'Joueur 2 remporte la partie', 7)
pyxel.run(update, draw)
