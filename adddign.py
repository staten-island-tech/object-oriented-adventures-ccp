import json
x=[{"name": "Pepper", "price": "5", "description": "Spicy for certain groups of people"}, {"name": "Salt", "price": "5", "description": "S"}, {"name": "Chicken", "price": "100", "description": "Popeyes and KFC"}, {"name": "Koolaid", "price": "80", "description": "Red Koolaid > Purple Koolaid"}, {"name": "Oil", "price": "20", "description": "America's favorite"}, {"name": "Watermelon", "price": "55", "description": "Fruit Ninja Master"}, {"name": "Lollipop", "price": "10", "description": "Chupa Chups"}, {"name": "Beef", "price": "50", "description": "Beef > Vegan Beef"}, {"name": "Broccoli", "price": "20", "description": "Earthy"}, {"name": "Bread", "price": "15", "description": "Doughy"}, {"name": "Butter", "price": "10", "description": "ICANTBELIEVETHATSNOTBUTTER!!!"}, {"name": "Marshmallow", "price": "15", "description": "who likes marshmallows by themselves?"}, {"name": "Chocolate", "price": "10", "description": "Dark and Milk Chocolate > White Chocolate"}, {"name": "Milk", "price": "15", "description": "Being lactose intolerant is a fate worse than death"}]
with open("json/NEWingredients.json", "w") as f:
    json.dump(x, f, indent=4)