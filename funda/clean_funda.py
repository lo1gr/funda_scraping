import json
import os 
import numpy as np
import re

print(os.getcwd())
with open('funda/quotes.json') as file:
    extract_data = json.load(file)

unique = []
def price_convert(_price): 
    # remove non alphanumeric char
    _price = re.sub(r'[,\.!?]', '', str(_price))
    # remove nonnumbers    
    # [^0-9]
    _price = re.sub(r'€', '', str(_price))
    # _price = re.sub(r'[^0-9]', '', str(_price))
    return _price
    # return float(re.sub(r'[^0-9.]|[^.]', '', str(_price)))

for el in extract_data:
        unique.append(price_convert(el['price']))
print(unique)

