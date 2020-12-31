# here we will be discussing all the important functions we might come across while building the computer vision projects

import cv2 as cv
import numpy as np


img=cv.imread('photos/cat2.jpg')
cv.imshow('colored img',img)
#converting an image to grescale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#bluring image
blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edging the images
canny=cv.Canny(img,200,200)
#this 200 and 200 are the threshild values they make the edge detectuon less and more sensitive
cv.imshow('Canny edges',canny)

#dialtions- making the edges more thicker
dilated=cv.dilate(img,(7,7),iterations=3)
cv.imshow('dilated',dilated)

#cropping 
cropped= img[50:200,200:400]
cv.imshow('cropped',cropped)


cv.waitKey(0)



