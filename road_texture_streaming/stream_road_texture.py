import carla
from PIL import Image

# connect to client and load Town02
client = carla.Client('127.0.0.1', 2000)
client.set_timeout(2.0)
world = client.get_world()

# set weather
weather = carla.WeatherParameters.ClearNoon
weather.sun_altitude_angle = 90
world.set_weather(weather)

# load texture image and create texture object
image = Image.open('textures/road_texture.png')
width, height = image.size
texture = carla.TextureColor(width, height)
for x in range(0,width):
    for y in range(0,height):
        color = image.getpixel((x,y))
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        a = 255
        texture.set(x, y, carla.Color(r,g,b,a))

# apply textures to the road
numbers = [85, 93,
           109, 117, 
           262, 184, 
           263, 185, 
           264, 186, 
           39, 35,
           31, 27,
           23, 19,
           15, 11,
           7, 3,
           142, 220,
           141, 219,
           140, 218]
object_names = ['Road_Road_Town02_113', 'Road_Road_Town02_105',
                'Road_Road_Town02_171', 'Road_Road_Town02_249', 
                'Road_Road_Town02_170', 'Road_Road_Town02_248',
                'Road_Road_Town02_169', 'Road_Road_Town02_247',
                'Road_Road_Town02_168', 'Road_Road_Town02_246']
for number in numbers:
    world.apply_color_texture_to_object('Road_Road_Town02_' + str(number), carla.MaterialParameter.Diffuse, texture)
    print('Applied texture to object')
