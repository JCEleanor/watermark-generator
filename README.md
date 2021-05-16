# Watermark-Generator


## Overview
A watermark generator built with Python and Pillow, which allows users to add watermark in the following positions:

![example](example_output/position_demo.jpg)

The program will first shrink the watermark 10x based on the input image's orientation. 

The math for each position is as below: 

<br>
1. upper left 
        
    watermark_position = (0, 0)
<br>
2. upper right 
       
    watermark_position = (input_width - logo_width, 0)
<br>
3. bottom right
        
    watermark_position = (input_width - logo_width, input_height - logo_height)
<br>
4. bottom left
        
    watermark_position = (0, input_height - logo_height)
<br>
5. center
        
    watermark_position = (input_width // 2, input_height // 2)


According to Cartesian pixel coordinate system, the origin (0, 0), is at the top left cornor, while the center of the watermark will actually be at (0.5, 0.5). 

## Requirements
Pillow: 

    
    pip install pillow
    

[Pillow Doc](https://pillow.readthedocs.io/en/stable/)

## Examples of Use
- Landscape

![example](example_output/IMG_8762.jpg)

- Profile

![example](example_output/IMG_221.jpg)

- Square

![example](example_output/IMG_1111.jpg)

## Future Improvement

- Intergrate Graphical User Interface such as Tkinter to improve user experience. 
- Add more flexibility to watermark position.
- Revamp error handling to make it more foolproof.
