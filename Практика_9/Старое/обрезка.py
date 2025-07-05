from PIL import Image
filename = 'icon.jpg'
img = Image.open(filename)
img.load()
res_img = img.resize((img.width // 8, img.height // 8))
res_img.save('res_icon.jpg')