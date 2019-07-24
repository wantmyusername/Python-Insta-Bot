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

MAX_W, MAX_H = 800, 800
im = Image.open("E:\\Bots\\Instagram Python Generador\\assets\\"+str(random.randint(0,1))+".png")
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("C:\\Users\\Jesus\\AppData\\Local\\Microsoft\\Windows\\Fonts\\HandsOn-Regular.ttf", 65)

#Este agrega el contenido (280px de arriba a abajo y 8 de espacios entre cada linea del texto
MAX_H, pad = 400,50
for line in para:
    w, h = draw.textsize(line, font=font)
    draw.text(((MAX_W - w) / 2, (MAX_H - h) /2 ), line, (255,255,255), font=font)
    MAX_H += h + pad


im.save(""+str(random.randint(0,99999))+".png", format="png")

#Esta funcion remueve la primer linea del documento
with open('contenido.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('contenido.txt', 'w') as fout:
    fout.writelines(data[1:])
