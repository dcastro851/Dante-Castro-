import picamera

#setup the camera 
camera = picamera.PiCamera()

#take picture
camera.capture('/home/pi/Desktop/cookie/image6.jpg')
