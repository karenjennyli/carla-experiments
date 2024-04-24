# Road_Road_Town10HD10

# import modules
import carla
import time, random
from PIL import Image

# original texture
image = Image.open('textures/T_Asphalt05_d.BMP')
height = image.size[1]
width = image.size[0]
print("Image size: ", width, "x", height)

# Connect to client
client = carla.Client('127.0.0.1', 2000)
client.set_timeout(2.0)
world = client.get_world()

# Instantiate a carla.TextureColor object and populate
# the pixels with data from the image
texture = carla.TextureColor(width ,height)
for x in range(0,width):
    for y in range(0,height):
        color = image.getpixel((x,y))
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        a = 255
        texture.set(x, y, carla.Color(r,g,b,a))

# every five seconds, apply the texture to the road, do it 10 times
for i in range(0,10):
    # add stripes to the road (400 pixels wide, 400 pixels apart), different color each time
    for x in range(0,width,400):
        color = carla.Color(r, g, b, a)
        for y in range(0,height):
            for j in range(0,200):
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                a = 255
                texture.set(x+j, y, color)
    world.apply_color_texture_to_object('Road_Road_Town10HD10', carla.MaterialParameter.Diffuse, texture)
    time.sleep(1)
