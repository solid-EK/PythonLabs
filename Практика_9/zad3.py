import csv
file = open('Products.csv', encoding='utf-8')
read = csv.DictReader(file)
sum = 0
print('Нужно купить:')
for row in read:
    print(f"{row['Продукт']} - {row['Количество']} шт. за {row['Цена']} рублей")
    sum += int(row['Цена']) * int(row['Количество'])
print('Итоговая сумма:', sum)