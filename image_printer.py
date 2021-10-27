from PIL import Image, ImageFont, ImageDraw
import pandas as pd

FONT_FILE = ImageFont.truetype(r'./times.ttf', 70)
FONT_COLOR = "#000000"
WIDTH, HEIGHT = 1900,1350


def make_cert(name):
    """function to generate certificate"""
    image_source = Image.open(r'./Hood club certificate_01.jpg')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text((WIDTH-name_width/2, HEIGHT-name_height/2), name, fill=FONT_COLOR, font=FONT_FILE)
    image_source.save("./out/" + name+".jpg")
    print('printing certificate of: '+name)


files=pd.read_excel("./Gaming Gangsta - attendance.xlsx")
names=files['Name']
for x in names:
    make_cert(x)