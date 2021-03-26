#Read a Video Stream from Camera (Frame by Frame)

import cv2

#0 here means the default web cam
cap = cv2.VideoCapture(0)

#Creating face detection object
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")


while True:
	ret,frame  = cap.read()
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


	#if camera not started yet
	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(gray_frame,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(248,145,31),2)

	cv2.imshow("Video Frame", frame)
	# cv2.imshow("Gray Frame", gray_frame)
	# cv2.imshow("HSV Frame", hsv_frame)

	
	#wait for the user input and then you will stop(imput: q)
	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()