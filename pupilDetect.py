# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

#create rectangular kernel of size 5x5
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	#take image and turn gray
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	#take gray and put it threw a threshold filter 
	retval, thresholded = cv2.threshold(gray, 5, 255, 0)

	#take thresholded that only sees black and find contours
	#im2, contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

	#drawing = np.copy(image)
	#cv2.drawContours(drawing, contours, -1, (255, 0, 0), 2)
	# show the altered frame
	cv2.imshow("Frame", thresholded)
	key = cv2.waitKey(30) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == 27:
		break
