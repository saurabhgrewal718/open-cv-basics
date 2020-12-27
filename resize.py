import cv2 as cv

#function to resize the video file 
#this method works for image,videosand live capture as well(we'll define a new method below which only works for the )
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#getting the video file 
capture = cv.VideoCapture('videos/video.mp4')

#looping through the video frames
# while True:
#     isTrue,frame = capture.read()
#     frameresized = rescaleFrame(frame,scale=0.25)

#     cv.imshow("video playingn",frame)
#     cv.imshow("resized video playing",frameresized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


#the rescaling of images is also possible 
img = cv.imread('photos/cat1.jpg')
resized_img = rescaleFrame(img)
cv.imshow("image not changed",img)
cv.imshow("rescaled",resized_img)

cv.waitKey(0)

#this function only works for the live video 
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)