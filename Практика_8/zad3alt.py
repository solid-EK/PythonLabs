import csv

file_path = 'Products.csv'
encoding = 'utf-8' # Или другая кодировка, если это необходимо

try:
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.DictReader(file)  # Используем DictReader для доступа к данным по именам столбцов
        print('Нужно купить:')
        for row in reader:
            # Доступ к элементам по ИМЕНАМ столбцов, а не индексам.  Замените 'название', 'количество', 'цена' на ваши реальные имена столбцов
            print(f"{row['Продукт']} - {row['Количество']} шт. за {row['Цена']} рублей")
except UnicodeDecodeError:
    print(f"Ошибка декодирования файла {file_path}. Проверьте кодировку.")
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
except KeyError as e:
    print(f"Ошибка: Столбец '{e.args[0]}' не найден в файле. Проверьте имена столбцов в файле CSV.")

