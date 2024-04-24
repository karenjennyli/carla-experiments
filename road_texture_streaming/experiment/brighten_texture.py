from PIL import Image

# load texture image
diffuse = Image.open('textures/Asphalt_d_4.BMP')
height_diffuse = diffuse.size[1]
width_diffuse = diffuse.size[0]
print('Loaded diffuse texture')

# create new texture image
diffuse_texture = Image.new('RGB', (width_diffuse, height_diffuse))
for x in range(0, width_diffuse):
    for y in range(0, height_diffuse):
        color = diffuse.getpixel((x,y))
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        # brighten the texture
        r = min(255, r + 75)
        g = min(255, g + 75)
        b = min(255, b + 75)
        diffuse_texture.putpixel((x,y), (r,g,b))

# save the new texture
diffuse_texture.save('textures/Asphalt_d_4_brightened.BMP')