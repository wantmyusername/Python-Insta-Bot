import os
import PIL
import random
import textwrap
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image, ImageDraw, ImageFont

astr = open("contenido.txt", "r").readline()
para = textwrap.wrap(astr, width=25)

MAX_W, MAX_H = 300, 300
im = Image.open("E:\\Bots\\Instagram Python Generador\\assets\\1.png")
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 35)

#Este agrega el contenido (280px de arriba a abajo y 8 de espacios entre cada linea del texto
current_h, pad = 200, 8
for line in para:
    w, h = draw.textsize(line, font=font)
    draw.text(((MAX_W - w) / 100 + 100, current_h), line, (255,255,255), font=font)
    current_h += h + pad

im.save("hola.png", format="png")

#Esta funcion remueve la primer linea del documento
with open('dias.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('dias.txt', 'w') as fout:
    fout.writelines(data[1:])
