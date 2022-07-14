## !pip install kwcoco -------- install this

import numpy as np
import random
import kwcoco
# import freetype
from PIL import ImageFont, ImageDraw, Image
import json
import os

font_path_json = 'fonts.json' 
with open(font_path_json) as file:
  fonts = json.loads(file.read())

words_path_json = 'words.json'
with open(words_path_json) as file:
  text = list(json.loads(file.read()).keys())

fontScale = 32 # font size
 
color = (0, 0, 0) # font color
output_path = 'sample_output' # path to save images
if not os.path.exists(output_path):
    os.makedirs(output_path+'\\images')

datafile = open(os.path.join(output_path,'datafile.txt'),'w')
no_images_per_font = 10 # number of images to generate

for font_name in fonts:
    for i in range(no_images_per_font):
        write = random.choice(text)
        text.remove(write)
        write = ''.join(random.choice((str.upper, str.lower))(c) for c in write)
        font = ImageFont.truetype(fonts[font_name], fontScale)
        img_size = list(font.getsize(write))
        img_size = img_size[::-1]
        img_size.append(3)
        blank_image = 255 * np.ones(img_size, dtype=np.uint8)
        image = Image.fromarray(blank_image)
        draw_img = ImageDraw.Draw(image)
        draw_img.text((0,0),write,font=font,fill=color)
        image.save(os.path.join(output_path,"images",font_name+'_'+write+'.jpg'))
        datafile.write(os.path.join(output_path,"images",font_name+'_'+write+'.jpg')+" "+write+"\n")
        # image.show()
        # break