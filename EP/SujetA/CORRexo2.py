def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2
    while i >= 0 and a < l[i]  :
      l[i+1] = l[i]
      l[i] = a
      i = i-1
    return l

assert insere(30, [10,20,40]) == [10, 20, 30, 40]
assert insere(-20, [10,20,40]) == [-20, 10, 20, 40]
assert insere(200, [10,20,40]) == [10, 20, 40, 200]
assert insere(20, []) == [20]
print('test OK')
