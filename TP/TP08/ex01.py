#1
def ensemble(chemin):
    E = set()
    f = open(chemin, "r", encoding="utf-8")
    for x in f:
        for i in x:
            E.add(i)
    return E
#2
def stat(chemin):
    dico = {}
    f = open(chemin, "r", encoding="utf-8")
    for x in f:
        for i in x:
            if i not in dico:
                dico[i] = 0;
            dico[i] = dico[i] + 1
    return dico
    
stat("dictionnaire.txt")
