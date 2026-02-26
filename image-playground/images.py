from PIL import Image, ImageFilter

#img = Image.open('./Pokedex/pikachu.jpg')
#filtered_img = img.filter(ImageFilter.BLUR)
#filtered_img.save("blur.png", "png")
#
#grey_img = img.convert('L')
#grey_img.save("grey.png", "png")
#
#rotated_img = img.rotate(90)
#rotated_img.save("rotated.png", "png")

img = Image.open('./astro.jpg')
print(img.size)
new_img = img.thumbnail((400, 400))
print(img.size)
img.save("thumbnail.jpg")