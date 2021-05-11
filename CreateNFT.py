
# -*- coding: utf-8 -*-
from bmp import BitMap, Color
from itertools import product
from random import randint, choice
import glob
from PIL import Image, ImageFont, ImageDraw
import B2Upload
from threading import Thread

DarkColors  = {
    "Green" : Color(0,102,0),
    "Cyan" : Color(0,102,102),
    "Blue" : Color(0,51,102),
    "DarkBlue": Color(0,0,102),
    "Orange": Color(153,76,0),
    "Yellow": Color(110,110,0),
    "Violet": Color(51,0,102),
    "Magenta": Color(102,0,102),
    "Pink": Color(102,0,51)
}
LightColors = {
    "Green" : Color(153,255,153),
    "Cyan" : Color(153,255,255),
    "Blue" : Color(152,204,255),
    "DarkBlue": Color(153,153,255),
    "Orange": Color(255,204,153),
    "Yellow": Color(255,255,153),
    "Violet": Color(204,153,255),
    "Magenta": Color(255,153,255),
    "Pink": Color(255,153,204)
}
SymbolCol = {
    "Red" : (255, 0 ,20),
    "Black" : (0,0,0)
}
Letter = ImageFont.truetype("Fonts/cardchar.ttf", 110)
Symbol = ImageFont.truetype("Fonts/cardchar.ttf", 190)
W = 406
L = 551
PIXEL_SIZE=29

#411 561
def Fillcolors(Amount, ChosenColor):
    AllColors = ChosenColor
    ColorArray = list()
    Colors = list()
    i = -1
    while i <  Amount:
        Col = choice(list(AllColors.keys()))
        if Col not in ColorArray:
            ColorArray.append(Col)
            i += 1
    for x in ColorArray:
        Colors.append(AllColors[x])      
    return Colors 

def CreateCard (card, Gen):
    cardschar = list()
    for c in card:
        cardschar.append(c)
    if cardschar[1] == '{' or cardschar[1] == '[':
        SymCol = SymbolCol["Red"]
        colors = Fillcolors(Gen, LightColors)
    else:
        SymCol = SymbolCol["Black"]
        colors = Fillcolors(Gen, LightColors)
    Filename = "Assests/test.png"
    bmp = BitMap(W,L)
    for x,y in product(range(W),range(L)):
        bmp.setPenColor(choice(colors))
        bmp.drawSquare(x*PIXEL_SIZE,y*PIXEL_SIZE,PIXEL_SIZE,fill=True)
    bmp.saveFile(Filename, compress=False)
    img = Image.open(Filename).convert('RGBA')
    width, height = img.size
    draw = ImageDraw.Draw(img)
    draw.text((24, 5),cardschar[0],font=Letter, fill=SymCol)
    draw.text((117, 153),cardschar[1],font=Symbol, fill=SymCol, anchor="mm")
    draw.text((312, 404),cardschar[0],font=Letter, fill=SymCol)
    img = img.convert('P', palette=Image.ADAPTIVE)
    img.save(Filename)
    #Thread(target=B2Upload.upload, args=(Filename, )).start()
    #print(B2Upload.upload(Filename))

CreateCard("7{", 4)


