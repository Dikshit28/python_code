from PIL import Image, ImageDraw, ImageFont
import os

image = Image.open("D:/python/bronze certi.jpeg")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("D:/python/times.ttf", 30)
try:
    os.mkdir('certificates')
except:
    pass
# enter the co-ordinates
# name
(x, y) = (615, 505)
color = 'rgb(0, 0, 0)'
draw.text((x, y), 'Dikshit', fill=color, size=100, font=font)
# marks
(x, y) = (577, 583)
color = 'rgb(0, 0, 0)'
draw.text((x, y), '50', fill=color, size=20, font=font)
filename = os.path.join('certificates', f"{'word'}_certificate.pdf")
image.save(os.path.join(filename))
