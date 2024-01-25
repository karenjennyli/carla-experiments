from PIL import Image

# BUILDING TEXTURE
original_texture = Image.open('T_Apartment04_D_Opt.TGA')
# get original size
original_width, original_height = original_texture.size

new_texture = Image.open('textures.png')
# cut off top half of image
# get size of image first
width, height = new_texture.size
new_texture = new_texture.crop((0, height/2, width, height))

# replace top left corner of original texture with new texture
original_texture.paste(new_texture, (0, 0))

# save new texture as a TGA
original_texture.save('T_Apartment04_D_Opt_modified.TGA')

# show textures
original_texture.show()
new_texture.show()


# BANNER TEXTURE
original_texture = Image.open('SM_banner_cDino.TGA')
# get original size
original_width, original_height = original_texture.size

new_texture = Image.open('dog.jpg')
# crop to match proportional dimensions of original texture, leaving middle of image
# get size of image first
width, height = new_texture.size
proportion = original_width/original_height
new_width = width
new_height = new_width/proportion
# resize to match original texture
new_texture = new_texture.resize((int(original_width), int(original_height)))
# save new texture as a TGA
new_texture.save('dog_banner.TGA')
# show textures
original_texture.show()
new_texture.show()