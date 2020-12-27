import cv2 as cv
#reading the image
# img = cv.imread('F:/machine learning projects/open cv projects/photos/cat1.jpg')
# img2 = cv.imread('photos/cat2.jpg')

# #show images
# cv.imshow("Cat2 picture",img2)
# cv.imshow('cat',img)

# #wait infinitely untill a key is pressed
# cv.waitKey(0)

#for videos
capture = cv.VideoCapture('videos/video.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow("video playingn",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
