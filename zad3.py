from PIL import Image
import os
os.mkdir('graypics')
for i in range(1, 6):
    filename = f"{i}.jpg"
    img = Image.open(filename)
    img.load()
    gray_img = img.convert('L')
    filename = f"gray{i}.png"
    gray_img.save(f'graypics\{filename}')