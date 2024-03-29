''' Realiza el <<Parsing>> del archivo .txt
    Separa los datos del archivo .txt en listas individuales
    con información de cada una de las públiciónes.

    (Datos aún no listos para realizar operaciones)
'''

from pprint import pprint

import glob





def parse_txt_to_lists():
    ''' Genera una lista de listas usando la información del archivo .txt de la BD
        -> [[a, b], [c, d], [e, f]]

        Parametros:
        --------------
        No

        Return: [[], [], [], ...]
        --------------
        Tipo: List
        Lista compuesta por listas de públicaciones

    '''

    PATH_TO_DATABASE = glob.glob("./input/*.txt")

    try:
        with open(PATH_TO_DATABASE[0], 'r') as publicaciones_bd:
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
    except:
        print("Error while reading file: charmap errror")
        return "Error - open /input/<*PubMed_Biomedicas*>"


if __name__ == '__main__':
    print("Not main app, run: python3 main_en.py")