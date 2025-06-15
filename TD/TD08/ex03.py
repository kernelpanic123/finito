contact = {'Chloe': '0601020304', 'Quentin': '0710203040', 'Lyes': '0623344556'}
#1
#contact['Chloe'] = '0611223344'


#2
#contact['Sarah'] = '0145444342'

#3
#contact['Lyes']

#4
#contact.pop('Chloe')

#5
def affichage(contacts):
    for k in contact:
        cle = contact[k]
        print(f"{k} : {cle}")
