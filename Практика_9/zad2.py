import json
with open('Products.json', 'r+', encoding='utf-8') as file:
    answer = input('Хотите добавить новую запись? ')
    if answer.lower() == 'да':
        data = json.load(file)
        name = input('Название: ')
        price = int(input('Цена: '))
        weight = int(input('Вес: '))
        available = input('Доступность (True/False): ').lower() == 'true'
        data['products'].append({"name": name, "price": price, "available": available, "weight": weight})
        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)
        file.truncate()
with open('Products.json', 'r', encoding='utf-8') as file:
    ld = json.load(file)
    for i in ld['products']:
        availability = "В наличии" if i['available'] else "Нет в наличии!"
        print(f"Название: {i['name']} \nЦена: {i['price']} \nВес: {i['weight']} \n{availability}")
