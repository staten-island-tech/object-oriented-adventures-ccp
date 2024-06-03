import json
with open("json/ingredients.json", "r") as f:
    data=json.load(f)
for i in data[0]:
    print(i)