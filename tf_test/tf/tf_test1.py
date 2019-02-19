import math
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
from PIL import ImageGrab
import _winapi

kernel_size = (5, 5);
sigma = 5;

img = cv2.imread('161.jpg')
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.imread('161.jpg',0)
print(img.shape)
img2 = img.copy()
template = cv2.imread('c1.png',0)
w, h = template.shape[::-1]
center_x=0
center_y=0
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF_NORMED']
time_start=time.time();
time_s=time_start
print('start')
for i in range(100):

    for meth in methods:
        img = img2.copy()
        method = eval(meth)
    
        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
#    print(res.shape)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)#找到最大值和最小值
        #print(cv2.minMaxLoc(res))
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img,top_left, bottom_right, 255, 2)

        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        if(center_x*center_y!=0):
            c_x=(top_left[0]+bottom_right[1])/2
            c_y=(top_left[1]+bottom_right[0])/2
            if abs(c_x-center_x)>10:
                center_x = (c_x+center_x)/2
            if abs(c_y-center_y)>10:
                center_y = (c_y+center_y)/2
        else:
            center_x=(top_left[0]+bottom_right[1])/2
            center_y=(top_left[1]+bottom_right[0])/2
    bbox=(center_x-150,center_y-200,center_x+150,center_y+100)
    cut = np.array(ImageGrab.grab().convert('RGB'))
    
    '''
    cut = ImageGrab.grab()

    
    name = 'E:/xxx/image'+ str(i%10) + '.png'
    cut.save(name)
    cut = cv2.imread(name)
    '''
    
    GImage=cv2.cvtColor(cut,cv2.COLOR_BGR2GRAY)
    ret,thresh4=cv2.threshold(GImage,127,255,cv2.THRESH_TOZERO)
    images = thresh4
    images = cv2.GaussianBlur(images,kernel_size,sigma)

time_end=time.time()
print (time_end-time_start)
plt.show(plt.imshow(images,'gray'))