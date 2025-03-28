from PIL import Image, ImageDraw, ImageFont
name = input('Кого вы хотите поздравить? ')
img = Image.open('деньцемента.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('HelveticaBlack.ttf', 40)
draw.text((700, 550), f'Поздравляю,{name}!', font=font, fill=(255, 255, 255), stroke_fill="black")
img.show()
