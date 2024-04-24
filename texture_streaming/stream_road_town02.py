import carla
from PIL import Image

# connect to client
client = carla.Client('127.0.0.1', 2000)
client.set_timeout(2.0)
world = client.get_world()
client.load_world('Town02')
print('Connected to world')

# original texture
image = Image.open('textures/filler_texture.png')
height = image.size[1]
width = image.size[0]
print('Loaded original texture with dimensions: ', width, 'x', height)
# 1024 x 1024

# set texture to image
texture = carla.TextureColor(width, height)
for x in range(0,width):
    for y in range(0,height):
        color = image.getpixel((x,y))
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        a = 255
        texture.set(x, y, carla.Color(r,g,b,a))
print('Set texture to image')

object_names = ['Road_Road_Town02_113', 'Road_Road_Town02_105',
                'Road_Road_Town02_171', 'Road_Road_Town02_249', 
                'Road_Road_Town02_170', 'Road_Road_Town02_248',
                'Road_Road_Town02_169', 'Road_Road_Town02_247',
                'Road_Road_Town02_168', 'Road_Road_Town02_246']
for object_name in object_names:
    world.apply_color_texture_to_object(object_name, carla.MaterialParameter.Diffuse, texture)
    print('Applied texture to object')