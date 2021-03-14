import json
import os 

print(os.getcwd())
with open('funda/quotes.json') as file:
    extract_data = json.load(file)

# join the keys together:
print(extract_data[0].keys())

