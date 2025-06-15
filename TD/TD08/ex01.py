#1
E = {'a','b','d','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

#2
def nb_occurrence(s):
    c = 0
    for i in s:
        if i in E:
            c = c + 1
    return c
#3
def ensemble_miniscules(s):
    E_min = set()
    for i in s:
        if i in E:
            E_min.add(i)
    return E_min
#4
def nb_minuscules(s):
    c = 0
    for i in s:
        if i in E:
            c = c + 1
    return c