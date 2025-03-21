from PIL import Image, ImageFont, ImageDraw
name = input('Введите название файла к которому вы хотите применить водяной знак: ')
water_text = input('Введите текст водяного знака: ')
size = int(input('Укажите размер шрифта: '))
img = Image.open(name)
img.load()
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('HelveticaBlack.ttf', size)
width, height = img.size
# font = ImageFont.load_default(32)
draw.text((width/2, height*0.75), water_text, font=font, fill=(31, 71, 136), anchor='mb')
img.show()