def pavage_triominos(n, i_trou, j_trou):

    if n < 2 :
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

        else : # trou à droite
            piece = (m,m-1,1)

    else : # trou en bas
        if j_trou < m :  # trou à gauche
            piece = (m-1,m,2)

        else : # trou à droite
            piece = (m-1,m-1,3)

    # chaque quart contient une coordonnée en moins, indiquée dans le dictionnaire dico_ij

    resultat.append(piece)

    decalage = {'HG' : (0,0), 'HD' : (..., ...), 'BG' : (...,...) , 'BD' : (...,...)}

    for k in decalage :
        i,j = dico_ij[k]
        i_decal,j_decal = decalage[k]
        res = pavage_triominos(m, ... ,... )
        if res is not [] :
            for p in res :
                resultat.append(  (..., ... , ...)   )

    return resultat
