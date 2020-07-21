# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:50:32 2020

@author: Valenzuela
"""

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
form = pd.read_excel("Participants.xlsx")
name_list = form['FirstName'].to_list()
name_list2 = form['LastName'].to_list()
a=-1
for i in name_list:
    a=a+1
    im = Image.open("rec.jpg")
    d = ImageDraw.Draw(im)
    location = (193, 555)
    location2 = (193, 725)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("arial.ttf", 100)
    d.text(location, i, fill=text_color, font=font)
    d.text(location2, name_list2[a], fill=text_color, font=font)
    im.save("certificate_" + i + ".pdf")