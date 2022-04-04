'''
    Remueve acentos, cacracteres y saltos de linea de la lista de listas generada con los nombres de los autores

    Genera una lista con los autores de cada publicación
'''

from pprint import pprint


with open('../../input/PubMed_Biomedicas_desde_2014.txt', 'r') as publicaciones_bd:
    raw_publicaciones_bd = list(publicaciones_bd.readlines())
    bulk_pub_conbo = []
    temp_pub_single = []
    for pub in raw_publicaciones_bd:
        if pub[:2] == 'SO':
            bulk_pub_conbo.append(temp_pub_single)
            temp_pub_single = []
        elif pub != '\n':
            temp_pub_single.append(pub)

# TODO agregar nested for
autores = []
for part in bulk_pub_conbo[0]:
    #print(type(part))
    if part[:2] == 'AU' or part[:3] == 'FAU':
        autores.append(part)
print(autores)
