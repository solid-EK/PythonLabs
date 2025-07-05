from PIL import Image, ImageFilter
import os
for i in os.listdir('input'):
    img = Image.open(f'input/{i}')
    img.load()
    edge_img = img.filter(ImageFilter.FIND_EDGES)
    filename = f"gray_{i}.png"
    edge_img.save(f"output/{filename}")