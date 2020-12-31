import cv2 as cv
import numpy as np 


blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#paint the image a certain color
# blank[:]=0,255,0
# cv.imshow('green',blank)

# blank[:]=255,0,255
# cv.imshow('different color thank green',blank)

#coloring a portion of image
# blank[200:300,300:400] = 0,0,255
# cv.imshow('certain portion',blank)

# #2- drawing a recatangle on the picture
# # cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
# # cv.imshow('rectangle',blank)

# #for the imgshape[1]=height an dimgshape[2]=width
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=2)
# cv.imshow('rectangle',blank)

# #3-circle
# cv.circle(blank,(250,250),40,(0,255,0),thickness=5)
# cv.imshow('circle',blank)

# #4-drawing a line
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,255),thickness=2)
# cv.imshow('line',blank)

#5-writing text
cv.putText(blank,'hello world',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text ',blank)

cv.waitKey(0)