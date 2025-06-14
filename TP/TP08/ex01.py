#1
def ensemble(chemin):
    E = set()
    f = open(chemin, "r", encoding="utf-8")
    for x in f:
        for i in x:
            E.add(i)
    return E
ensemble("dictionnaire.txt")