import cv2
import time
import os
import keyboard
import winsound
import threading
import pyautogui
import numpy as np
import pyttsx3


from image_Classifier.imageClassifier import imageClassification
from Evaluation import get_letter

def processImage(frame):
	h, w, channels = frame.shape
	half = w//2
	left_part = frame[:, :half]
	right_part = frame[:, half:]
	return right_part,left_part


def all_equal(lst):
	if all(x == lst[0] for x in lst) and lst:
		return True
	return False


def all():
	engine = pyttsx3.init()
	cam = cv2.VideoCapture(1)
	nextLeter = True
	prevLeter = None
	enablePress = True
	nextLeterFlag = True
	datamatrix = np.zeros((6,6))
	capsLock = False

	while True:
		ret,frame = cam.read()
		cv2.imshow('frame', frame)
		if not ret:
		    print("Failed")
		else:
			rightData,leftData = imageClassification(frame)
			

			dataTemp = leftData.T*rightData
			datamatrix = (datamatrix+dataTemp)/2

			max_index = np.argmax(datamatrix) 
			max_index_row = max_index // datamatrix.shape[1]
			max_index_col = max_index % datamatrix.shape[1]


			if datamatrix[max_index_row,max_index_col]<0.7:
				max_index_row = 5
				max_index_col = 5
				nextLeter = True
				
				
				if nextLeterFlag:
					engine.say("next")
					engine.runAndWait()
					nextLeterFlag = False


			leter = get_letter(str(max_index_col),str(max_index_row))
			
			if enablePress:
				if leter == 'enable':
					engine.say("Enable Press False")
					engine.runAndWait()
					time.sleep(2)
					engine.say("Deactivated")
					engine.runAndWait()
					enablePress = False
				elif leter == 'capsLock':
					if capsLock:
						engine.say("Capital Leter Disabled")
						engine.runAndWait()
						capsLock = False
					else:
						engine.say("Capital Leter Enabled")
						engine.runAndWait()
						capsLock = True
				elif leter in ['backspace' or 'enter']:
					engine.say(str(leter))
					engine.runAndWait()
					pyautogui.press(leter)
					prevLeter = leter
					nextLeter = False
					nextLeterFlag = True
				elif leter and nextLeter:
					if capsLock:
						leter = leter.upper()
					engine.say(str(leter))
					engine.runAndWait()
					pyautogui.press(leter)
					prevLeter = leter
					nextLeter = False
					nextLeterFlag = True
			
			else:
				if leter == 'enable':
					engine.say("Enable Press True")
					engine.runAndWait()
					time.sleep(2)
					engine.say("Activated")
					engine.runAndWait()
					enablePress = True
				elif leter == 'capsLock':
					if capsLock:
						engine.say("Capital Leter Disabled")
						engine.runAndWait()
						capsLock = False
					else:
						engine.say("Capital Leter Enabled")
						engine.runAndWait()
						capsLock = True
				elif leter and nextLeter:
					engine.say(str(leter))
					engine.runAndWait()
					print("Pressed: "+leter)
					prevLeter = leter
					nextLeter = False
					nextLeterFlag = True
			
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cam.release()
	cv2.destroyAllWindows()	


if __name__ == "__main__":
    all()
     


