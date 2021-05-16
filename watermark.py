import os
from PIL import Image
import time
from datetime import date
import re

def watermark_img(orgnl_file, watermark, pos, output_file):
    global pic_count
    pic_count = 0
    for folder , sub_folders , files in os.walk(orgnl_file):
        for file in files:
            #this will ignore every other file that's not jpg
            if file.endswith(".jpg") or file.endswith(".JPG"):

                pic = Image.open(f"{folder}/{file}")

                pic_x, pic_y = pic.size

                logo = Image.open(watermark)

                if pic_x > pic_y:     
                    logo.thumbnail((pic_x//10,pic_y//10)) #resize according to width
                else:
                    logo.thumbnail((pic_y//10,pic_x//10)) #resize according to highth
                    
                if pos == 1:
                    position = (0,0) #upper left
                elif pos == 2:
                    position = (pic_x-logo.size[0],0) #upper right
                elif pos == 3:              
                    position = (pic_x-logo.size[0], pic_y-logo.size[1]) #bottom right
                elif pos == 4:
                    position = (0,pic_y-logo.size[1]) #bottom left
                else:
                    position = (pic_x//2, pic_y//2) #center
                    
                pic.paste(logo, position, mask=logo)
#                 pic.show()
                
                pic.save(output_file+ re.findall(r'/.*' ,pic.filename)[0])
                pic_count+=1

def get_position():
    decision = int(input('Choose a location, upper left (1), upper right(2), bottom right(3), bottom left(4) or center(5): ')) 
    return decision

def get_output_file_name():
    today = date.today()
    path = today.strftime("%y%m%d")
    if not os.path.exists(path):
                os.makedirs(path)
    return path #'210110'

def main():
    
    tic = time.perf_counter()
    print('##########All image files must be JPG file##########')
    original_file = input('Enter image folder name: ')
    watermark = input('Choose your watermark (must be a png file): ') + '.png'
    position = get_position()
    output_file = get_output_file_name()
    
    watermark_img(original_file, watermark, position, output_file)
    
    toc = time.perf_counter()
    print(f'\nTotal: {pic_count}\nFinished in {round(toc-tic)} seconds')
    print('Image(s) successfully watermarked and saved to folder named ',get_output_file_name())

main()