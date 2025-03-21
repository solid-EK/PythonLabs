from PIL import Image
filename = 'aphex.png'
img = Image.open(filename)
img.load()
res_img = img.resize((img.width // 3, img.height // 3))
horiz_img = res_img.transpose(Image.FLIP_LEFT_RIGHT)
vert_img = res_img.transpose(Image.FLIP_TOP_BOTTOM)
res_img.save('aphex_res.png')
horiz_img.save('aphex_horiz.png')
vert_img.save('aphex_vert.png')