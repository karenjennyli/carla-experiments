from PIL import Image

original_texture = Image.open('T_Apartment04_D_Opt.TGA')
# get original size
original_width, original_height = original_texture.size

new_texture = Image.open('dog.jpg')

# replace top left corner of original texture with new texture
original_texture.paste(new_texture, (0, 0))

# save new texture as a TGA
original_texture.save('dog.TGA')

# show textures
original_texture.show()
new_texture.show()