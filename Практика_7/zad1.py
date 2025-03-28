from PIL import Image
img = Image.open('8march.gif')
cropimg = img.crop((50,0,250,400))
cropimg.save('croppostcard.png')