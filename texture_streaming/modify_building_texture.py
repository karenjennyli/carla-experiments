from PIL import Image, ImageOps

# original building texture
original_texture = Image.open('T_Apartment04_D_Opt.BMP')
original_texture.show()

# invert building texture colors
inverted_texture = ImageOps.invert(original_texture)
inverted_texture.show()

# save inverted texture
inverted_texture.save('T_Apartment04_D_Opt_inverted.BMP')