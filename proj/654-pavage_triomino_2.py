"""
https://e-nsi.gitlab.io/pratique/N3/654-pavage_triomino_2/sujet/
"""
def pavage_triominos(n, i_trou, j_trou):
    resultat = []
    if n == 1 :
        return []
    m = n//2
    dico_ij = {'HG' : (m-1, m-1),
            'HD' : (m-1, m),
            'BG' : (m,m-1) ,
            'BD' : (m,m)
            }
    if i_trou < m : # trou en haut
        if j_trou < m :  # trou à gauche
            piece = (m,m,0)
            dico_ij['HG'] =  (i_trou, j_trou)
        else : # trou à droite
            piece = (m,m-1,1)
            dico_ij['HD'] =  (i_trou, j_trou)
    else : # trou en bas
        if j_trou < m :  # trou à gauche
            piece = (m-1,m,2)
            dico_ij['BG'] =  (i_trou, j_trou)
        else : # trou à droite
            piece = (m-1,m-1,3)
            dico_ij['BD'] =  (i_trou, j_trou)
    # chaque quart contient une coordonnée en moins, indiquée dans le dictionnaire dico_ij

    resultat.append(piece)

    decalage = {'HG' : (0,0), 'HD' : (0, m), 'BG' : (m,0) , 'BD' : (m,m)}

    for k in decalage :
        i,j = dico_ij[k]
        i_decal,j_decal = decalage[k]
        res = pavage_triominos(m, i- i_decal,j-j_decal)
        if res is not [] :
            for p in res :
                resultat.append(  (p[0]+i_decal, p[1]+j_decal, p[2])  )

    return resultat


# tests
assert est_pavage(2, 1, 1, pavage_triominos(2, 1, 1)) == True

assert est_pavage(4, 0, 1, pavage_triominos(4, 0, 1)) == True

assert est_pavage(8, 5, 4, pavage_triominos(8, 5, 4)) == True

