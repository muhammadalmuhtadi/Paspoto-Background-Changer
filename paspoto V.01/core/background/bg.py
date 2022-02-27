from PIL import Image
from .color import warna


def fillbg(image, bg=None):
    
    if bg:
        im = Image.open(image)
        
        fill_color = warna[bg]  # your new background color

        im = im.convert("RGBA")   # it had mode P after DL it from OP
        if im.mode in ('RGBA', 'LA'):
            background = Image.new(im.mode[:-1], im.size, fill_color)
            background.paste(im, im.split()[-1]) # omit transparency
            im = background

        im.convert("RGB").save("static/results/output.png")
                

    else:
        return None