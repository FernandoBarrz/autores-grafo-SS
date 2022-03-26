''' Realiza el <<Parsing>> del archivo .txt
    Separa los datos del archivo .txt en listas individuales
    con información de cada una de las públiciónes.

    (Datos aún no listos para realizar operaciones)
'''

from pprint import pprint


def parse_txt_to_lists():
    ''' Genera una lista de listas usando la información del archivo .txt de la BD
        -> [[a, b], [c, d], [e, f]]

        Parametros:
        --------------
        No

        Return:
        --------------
        Tipo: List
        Lista compuesta por listas de públicaciones

    '''

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
    return bulk_pub_conbo



bulk = parse_txt_to_lists()
pprint(bulk)
print(bulk.__len__())



