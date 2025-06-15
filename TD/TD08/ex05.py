#1
def sauvegarde(contact, chemin):
    f = open(chemin , 'w', encoding='utf-8')
    for k in contact:
        i = contact[k]
        f.write(f"{k},{i}\n")
    f.close()
    
#2
def decouper(chaine):
    return chaine.split(",")
    