import json
import os 
import numpy as np

print(os.getcwd())
with open('funda/quotes.json') as file:
    extract_data = json.load(file)

# join the keys together:
dico = {}
total_elements = 0

for el in extract_data:
    total_elements += len(el["price"])

# Join all the elements: price together...
price, address, size1, size2, rooms, link = ([],)*6

# def append_val(val, el):
#     print(str(val))
#     return np.append(val, el[str(val)])

for el in extract_data:
    # for key in el.keys():
    print('-----------------------')
    print(str(len(el["price"])))
    print(str(len(el["address"])))
    print(str(len(el["size1"])))
    print(str(len(el["size2"])))
    print(str(len(el["rooms"])))
    print(str(len(el["link"])))
    # price = np.append(price, el["price"])
    # address = np.append(address, el["address"])
    # size1 = np.append(size1, el["size1"])
    # size2 = np.append(size2, el["size2"])
    # rooms = np.append(rooms, el["rooms"])
    # link = np.append(link, el["link"])


print(price)
print(str(len(price)) + " " + str(len(address)) + " " + str(len(size1)) + " " + str(len(size2)) + " " + str(len(rooms)) + " " + str(len(link))) 


# for house_no in range(1,total_elements+1):
#     dico[house_no]['price'] = 
#     dico[house_no]['address']
#     dico[house_no]['size1']
#     dico[house_no]['size2']
#     dico[house_no]['rooms']
#     dico[house_no]['link']

    


