from PIL import Image
import asyncio

async def photo_to_gif_with_duck(input_photo_path):
    photo = Image.open(input_photo_path).convert('RGBA')
    duck = Image.open('png/duck.png')
    duck_new_height = photo.height // 4
    duck_new_width = round((duck_new_height / duck.height) * duck.width)
    new_duck = duck.resize((duck_new_width, duck_new_height)).convert('RGBA')
    duck_reversed = Image.open('png/duck_reversed.png').resize((duck_new_width, duck_new_height)).convert('RGBA')
    x_duck = 0
    frames = []
    for i in range(1,11):
        await asyncio.sleep(0.1)
        step = round((photo.width - new_duck.width)/9)
        photo = Image.open(input_photo_path).convert('RGBA')
        photo.paste(new_duck, (x_duck, photo.height - duck_new_height), new_duck)
        photo.save(f'gif/temp/duck_{i}.png')
        x_duck += step
        frames.append(Image.open(f'gif/temp/duck_{i}.png'))
    xx_duck = photo.width - new_duck.width
    for i in range(11, 21):
        await asyncio.sleep(0.1)
        step = round((photo.width - new_duck.width)/9)
        photo = Image.open(input_photo_path).convert('RGBA')
        photo.paste(duck_reversed, (xx_duck, photo.height - duck_new_height), duck_reversed)
        photo.save(f'gif/temp/duck_{i}.png')
        xx_duck -= step
        frames.append(Image.open(f'gif/temp/duck_{i}.png'))
    return frames[0].save('gif/duck.gif', save_all=True, append_images=frames[1:], optimize = True, duration = 150,loop=0)



