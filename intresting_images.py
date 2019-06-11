import numpy as np
import PIL
from random import randint

def random_color_img():
    '''Creates a 400*400 image where each pixel displayed is of a random color
    '''
    new=PIL.Image.new('RGB',(400,400),(0,0,0))
    array=np.array(new)
    for r in range(len(array)):
        for c in range(len(array[0])):
            array[r][c]=[randint(0,225),randint(0,225),randint(0,225)]
    final=PIL.Image.fromarray(array)
    final.save('randomcolor.jpg')

def empty_img():
    '''Creates a 100*100 image which is fully transparent'''
    empty = PIL.Image.new('RGBA', (100,100), (0,0,0,0))
    empty.save('Empty.jpg')