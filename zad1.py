from PIL import Image
filename = 'aphex.png'
with Image.open(filename) as img:
    img.load()
    img.show()
    print(img.format)
    print(img.size)
    print(img.mode)