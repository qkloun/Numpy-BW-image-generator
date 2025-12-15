import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys


def image_load(filename):
    return plt.imread(filename)


def img2gray(img):
    gray = np.dot(img[...,0:3],[0.299,0.587,0.114])
    gray = np.stack([gray, gray, gray], axis=-1)
    
    
    return gray
    

def Animation(img,gimg,steps=30):
    
    svalues = np.hstack([np.linspace(0.0, 1.0, steps), np.linspace(1.0, 0, steps)])
    
    img_float = img.astype(np.float32)
    gimg_float = gimg.astype(np.float32)
    
    images = [np.uint8(img_float * (1.0 - s) + gimg_float * s) for s in svalues]
    
    while True: # repeat all images in a loop
        for imgs in images:
            yield imgs
    

fig = plt.figure()
im = plt.imshow(image_load("florida-keys-800-480.jpg"), interpolation='none',
animated=True)

img = image_load("florida-keys-800-480.jpg")
grayimg = img2gray(img)

imggen = Animation(img,grayimg)

def updatefig(*args):
    global imggen
    img_array = next(imggen) # get next image animation frame
    im.set_array(img_array) # set it. FuncAnimation will display it
    return (im,)

ani = animation.FuncAnimation(fig, updatefig, interval=60, blit=False)

plt.show()
