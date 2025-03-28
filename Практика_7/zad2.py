from PIL import Image, ImageDraw
import os
postcards = {'8 марта': '8march.gif', 'яблочный спас': 'яс.jpg', 'день цемента': 'деньцемента.jpg'}
hd = input('К какому празднику вы хотите открытку? ')
if hd.lower() in postcards:
    img = Image.open(postcards[hd.lower()])
    img.show()
else:
    print('Такого праздника у нас нет(')