
import numpy as np
import cv2


img1 = cv2.imread('GameStream/1019.BMP')
img2 = cv2.imread('GameStream/1020.BMP')
Gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
Gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
diff = cv2.absdiff(Gray1,Gray2)

'''
img_medianBlur=cv2.medianBlur(diff,5)
gimg=cv2.GaussianBlur(diff,(7,7),sigmaX=0)
#NoiseImg=SaltAndPepper(gimg,0.4)
#h=cv2.cvtColor(diff,cv2.COLOR_BGR2HSV)
#Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
lower_white=np.array([254,254,254])
upper_white=np.array([255,255,255])
lower_black=np.array([60,60,60])
upper_black=np.array([255,255,255])
mask1 = cv2.inRange(img1, lower_white, upper_white)
mask2 = cv2.inRange(img_medianBlur, lower_black, upper_black)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))  
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) 
close = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel2)
opening = cv2.morphologyEx(close, cv2.MORPH_OPEN, kernel1)
'''
cv2.imshow('',diff)
cv2.waitKey(0)

a = 70
print(chr(a))
b = 'F'
print(ord(b))
