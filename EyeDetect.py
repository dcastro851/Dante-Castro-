import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_eye.xml')
 
#the zero signifies which camera
cap = cv2.VideoCapture(0)

while 1:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	eyes = eye_cascade.detectMultiScale(gray)
	for(ex,ey,ew,eh) in eyes:
		cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		roi_gray2 = gray[ey:ey+eh, ex:ex+ew]
        	roi_color2 = img[ey:ey+eh, ex:ex+ew]
		circles = cv2.HoughCircles(roi_gray2,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
		try:
			for i in circles[0,:]:
				#draw the outer circle
				cv2.circle(roi_color2,(i[0],i[1]),i[2],(255,255,255),2)
				print("drawing circle")
				#draw the center of the circle
				cv2.circle(roi_color2,(i[0],i[1]),2,(255,255,255),3)
		except Exception as e:
			print e
	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
