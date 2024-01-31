# Road_Sidewalk_Town10HD11

from PIL import Image, ImageOps

# original texture
original_texture = Image.open('textures/T_Sidewalk_01_d.BMP')

# invert texture colors
inverted_texture = ImageOps.invert(original_texture)

# save inverted texture
inverted_texture.save('textures/T_Sidewalk_01_d_inverted.BMP')

# import modules
import sys
try:
    sys.path.append('/home/karenli/carla/PythonAPI/carla/dist/carla-0.9.14-py3.8-linux-x86_64.egg')
except IndexError:
    print('Error: CARLA PythonAPI not found.')
    pass

import carla
from PIL import Image

# Connect to client
client = carla.Client('127.0.0.1', 2000)
client.set_timeout(2.0)
world = client.get_world()

# Load the modified texture
image = Image.open('textures/T_Sidewalk_01_d_inverted.BMP')
height = image.size[1]
width = image.size[0]

# Instantiate a carla.TextureColor object and populate
# the pixels with data from the modified image
texture = carla.TextureColor(width ,height)
for x in range(0,width):
    for y in range(0,height):
        color = image.getpixel((x,y))
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        a = 255
        texture.set(x, y, carla.Color(r,g,b,a))

# Now apply the texture to the building asset
world.apply_color_texture_to_object('Road_Sidewalk_Town10HD11', carla.MaterialParameter.Diffuse, texture)
