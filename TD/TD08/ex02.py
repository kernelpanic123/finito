#1
def jour(s):
    with open(s, 'w') as fichier:
        for heure in range(24):
            for minute in range(0, 60, 5):
                ligne = f'{heure:02}:{minute:02}\n'
                fichier.write(ligne)

    