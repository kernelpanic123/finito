# [1,2,3,4] [1,2,3,4] car partage la meme memoire
# [1, 2, 3, 4, 3] [1, 2, 3, 4]
# [1, 2, 3, 4, 3] [1, 2, 3, 4, 7]

#2
def copier_liste(L):
    L2 = []
    for x in L:
        L2.append(x)
    return (L2)
#Oui, il permet de copier des matrices car une matrice est tout simplement une liste de liste.
