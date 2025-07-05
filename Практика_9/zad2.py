from PIL import Image
import os
type = input('Введите формат, который вам нужен: ')
print('Имя Разрешение Формат Режим')
for i in os.listdir('input'):
    img = Image.open(f'input/{i}')
    if img.format == type.upper():
        print(i, img.size, img.format, img.mode)
    else:
        print(i, 'Неподходящий формат')