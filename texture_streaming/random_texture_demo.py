# import modules
import sys
try:
    sys.path.append('/home/karenli/carla/PythonAPI/carla/dist/carla-0.9.14-py3.8-linux-x86_64.egg')
except IndexError:
    print('Error: CARLA PythonAPI not found.')
    pass

import carla
import random

# Connect to client
client = carla.Client('127.0.0.1', 2000)
client.set_timeout(2.0)
world = client.get_world()

# Get names of all available objects
object_names = world.get_names_of_all_objects()
for name in object_names:
    print(name)

'''
# Choose an object to modify # For example target_object could be 'SM_Cartel_Add_5'
target_object = random.choice(object_names)
print('Altering texture for object: ' + target_object)

# Modify its texture
texture = carla.TextureColor(width,height)
for x in range(0,len(image[0])):
    for y in range(0,len(image)):
        color = image[y][x]
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        a = int(color[3])
        texture.set(x, height - y - 1, carla.Color(r,g,b,a))
world.apply_color_texture_to_object(target_object, carla.MaterialParameter.Diffuse, texture, 0)
'''