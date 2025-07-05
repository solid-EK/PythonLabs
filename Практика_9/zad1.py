import json
file = open('Products.json', encoding='utf-8')
ld = json.load(file)
for i in ld['products']:
    availability = "В наличии" if i['available'] else "Нет в наличии!"
    print(f"Название: {i['name']} \nЦена: {i['price']} \nВес: {i['weight']} \n{availability}")
