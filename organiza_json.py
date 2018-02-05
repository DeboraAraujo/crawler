# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import json

with open('C:/Users/debor/Documents/crawler/reviews.json', encoding='utf-8') as json_data:
    d = json.load(json_data)
    #print(d[0])
    
reviews = []
for i in range(0,len(d)):
    split_line = str(d[i]).split("<br>")
    merge_line = ""
    
    for j in range(1,len(split_line)):
        merge_line += split_line[j]
        merge_line = merge_line.replace("</div>","")
        merge_line = merge_line.replace("<strong>","")
        merge_line = merge_line.replace("</strong>","")
        
    reviews.append(merge_line)

#print(reviews)

reviews_salvar = [
        
        dict(comentario=obj)
        for obj in reviews

        ]

dict_salvar = {"reviews": reviews_salvar}
dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)
try:
    arquivo_json = open("C:/Users/debor/Documents/crawler/reviews_organizados.json", "w")
    arquivo_json.write(dict_salvar)
    arquivo_json.close()
except:
    print("Error")