
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


# count_n = 0
# for publicacion in bulk_pub_conbo:
#     for part in publicacion:
#         if 'PMID' in publicacion[1]:
#             print("OK")
#         else:
#             print("fathal error")


print(bulk_pub_conbo.__len__())
#print(f"HEEEYYY  -> {count_n}")
#print(bulk_pub_conbo)

#        if pub[:4] == 'PMID':
#            temp_pub_single.append(pub)
    #raw_publication_bd = "".join(raw_publication_bd)


#with open('./prueba.txt', 'w') as prueba:
#    prueba.writelines(bulk_pub_conbo)



