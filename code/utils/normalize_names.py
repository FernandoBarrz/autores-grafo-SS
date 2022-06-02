from pprint import pprint


def normalize(string):
    ''' Reemplaza las letras con tildes de una cadena de texto
        Args: 
            El caracter a reemplzar
        Return:
            Catacter sin tilde
    '''

    table = {  
            'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o',
            'ú': 'u'
    }
    
    string = string.lower()

    string_T = string.maketrans(table)
    
    return string.translate(string_T).lower().replace("-", "").replace(",", "")




#nombre_cumpleto = ["memo", "leticia", "rocha", "zavaleta", 'paco']

#nombre_colab =['rocha', 'zavaleta', 'leticia']


#for nombre in nombre_cumpleto:
#  if nombre in nombre_colab:
#    print(f'{nombre} esta en bi')
#  else:
#    print(f'{nombre} NOOO esta en bi')




# TODO refactor to remove trailing \n

def cap_names_raw():
    with open('./input/nombre-investigadores.txt', 'r') as nombres_inv:
        lista_nombres_raw = list(nombres_inv.readlines())
        lista_nombres_capitalized = []
        for nombre in lista_nombres_raw:
            lista_nombre = nombre.split(' ')

            temp_nombre = lista_nombre[1:-1]
            temp_nombre = "-".join(temp_nombre)
            temp_nombre = temp_nombre.title()
            lista_nombres_capitalized.append(temp_nombre)

    return lista_nombres_capitalized
        
if __name__ == '__main__':
    print(cap_names_raw())
    print("Not main app, run: python3 main_en.py")