from PIL import Image

textures = ['T_Asphalt02_d.TGA', 'T_Asphalt02_n.TGA', 'T_Asphalt05_ORMH.TGA']

for texture in textures:
    original = Image.open('textures/' + texture)
    height = original.size[1]
    width = original.size[0]
    resized = original.resize((int(width/10), int(height/10)))
    if len(resized.getbands()) == 3:
        resized_tiled = Image.new('RGB', (width, height))
    else:
        resized_tiled = Image.new('RGBA', (width, height))
    for x in range(0, width, int(width/10)):
        for y in range(0, height, int(height/10)):
            resized_tiled.paste(resized, (x, y))
    resized_tiled.save('textures/' + texture[:-4] + '_tiled.TGA')
