density = 50

#Image to index with color====================

import numpy as np
colors = np.array([[152, 215, 255],[255, 255, 255],[117, 174, 72],[103, 76, 53],[100, 101, 102], None,[48, 146, 32],[217, 208, 158],None,[41, 51, 182], None,None,None,None,None], dtype=object)#minecraft optimized
def nearestColor(c):
    nearestColor = None
    index = -1
    minDist = 100000#positive infinity
    for i, color in enumerate(colors):
        if color is None:
            continue
        dr = abs(c[0]-color[0])
        dg = abs(c[1]-color[1])
        db = abs(c[2]-color[2])
        dist = dr+dg+db
        if dist < minDist:
            minDist = dist
            nearestColor = color
            index = i
    return nearestColor, index


from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open('test.png')
image = image.resize((density, density))
indexes = np.zeros((density, density))


rgb_im = image.convert('RGB')#RGB

plt.imshow(rgb_im, interpolation="None")

size = rgb_im.size

#loop
#x
for x in range(size[0]):
    #y
    for y in range(size[1]):
        rgb = rgb_im.getpixel((x,y))
        rgb, i = nearestColor(rgb)
        indexes[x,y] = i
        #set pixel
        #rgb_im.putpixel((x,y),(r,g,b,1))
        rgb_im.putpixel((x,y),(rgb[0],rgb[1],rgb[2],1))

#show
#im2.show()

#plt.imshow(indexes.transpose(), interpolation="None")
plt.imshow(rgb_im, interpolation="None")

#Draw with pyautogui======================

import math
import pyautogui as pag

def boxCenter(box):
    return box.left+box.width/2, box.top+box.height/2

aib = pag.locateOnScreen("air.png", confidence=0.94)
stb = pag.locateOnScreen("stonewall.png", confidence=0.94)
aix, aiy = boxCenter(aib)
stx, sty = boxCenter(stb)

def materialSelect(index):
    i = index%5
    j = math.floor(index/5)
    x = aix+(stx-aix)*i/4
    y = aiy+(sty-aiy)*j/2
    pag.click(x, y)
    
import pyautogui as pag
import numpy as np
from time import sleep



tlb = pag.locateOnScreen("tl.png", confidence=0.94)
brb = pag.locateOnScreen("br.png", confidence=0.94)
tlx, tly = boxCenter(tlb)
brx, bry = boxCenter(brb)


#pag.click(tlb)
#materialSelect(4)
#materialSelect(0)


pag.click(tlb)
xs = np.linspace(tlx, brx, density)
ys = np.linspace(tly, bry, density)
for i in range(density):
    for j in range(density):
        x = xs[i]
        y = ys[j]
        index = indexes[i,j]
        materialSelect(index)
        pag.click(x, y)
