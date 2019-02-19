#-*-encoding:utf-8-*-

import pytesseract
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import cv2
import math
import time
tessdata_dir_config = '--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR"'

class GetImageDate(object):
    def m(self):
        img = cv2.imread('3.jpg')

        #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
        #GrayImage0=cv2.cvtColor(im[0],cv2.COLOR_BGR2GRAY)
        #mask = cv2.inRange(img, lower_white, upper_white)
        mask = cv2.inRange(img, lower_black, upper_black)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))  
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  
        #cv2.imshow('Mask', mask)
        #cv2.waitKey(0)
        
        #image = Image.open('3.png')
        text = pytesseract.image_to_string(opening,config=tessdata_dir_config)
        #print (text)
        return text

    def SaveResultToDocument(self):
        text = self.m()

    def GetHeart(self):
        image = cv2.imread('heart.jpg')
        mask = cv2.inRange(image, lower_white, upper_white)
        ret, binary = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)  
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  
        opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel) 
        opening,contours, hierarchy = cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        print (len(contours))  #血量个数统计出来啦
        '''
        cv2.imshow('Mask', image)
        cv2.waitKey(0)
        '''

    def CheckDead(self):
        image = cv2.imread('13A806C0A41F4E2271FFE6E79D56600B.jpg')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template= cv2.imread('template.jpg',0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.75
        loc = np.where( res >= threshold)
        if len(loc[0])==0:
            print('0')
        else:
            print('1')
        
        #for pt in zip(*loc[::-1]):
        #    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), 255, 2)
        #cv2.imshow('',image)
        #cv2.waitKey(0)


# set white thresh
lower_white=np.array([200,200,200])
upper_white=np.array([255,255,255])
lower_black=np.array([0,0,0])
upper_black=np.array([20,20,20])
dead_check_num = 0
g = GetImageDate()
time_start=time.time()
for i in range(100):
    g.SaveResultToDocument()
#g.GetHeart()
#time_start=time.time()
#g.CheckDead()
time_end = time.time()
time = time_end-time_start
print(time)
