#CÓDIGO UTILIZADA PARA AGRUPAR 

import pandas as pd
import json

urls = pd.read_csv("urls.csv",header=None)[0]

stores = ["casasbahia","mercadolivre","magazineluiza"]
lists = []
files = []

for store in stores:
    l = []
    lists.append(l)
    f = open("urlsBuffers/" + str(store),'w')
    files.append(f)


for url in urls: 
    for (index,store) in enumerate(stores):
        if store in url:
            lists[index].append(url)

for (l,f) in zip(lists,files):
    json.dump(l,f)