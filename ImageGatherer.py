import cv2
import time
import os
import keyboard
import winsound


def detectKeyPress():
    alphabet2 = "º012345"
    for leter in alphabet2:
        if keyboard.is_pressed(leter):
            print("detected"+str(leter))
            return leter
    return ""

def saveImage(img_coutner,leter,frame):
    img_name = "opencv_frame{}.png".format(img_coutner)
    h, w, channels = frame.shape
    half = w//2
    left_part = frame[:, :half]
    right_part = frame[:, half:]
    pathR = 'C:/Users/polgo/Desktop/Tiny Test/Right/{}'.format(leter)
    pathL = 'C:/Users/polgo/Desktop/Tiny Test/Left/{}'.format(leter)
    print(pathR)
    cv2.imwrite(os.path.join(pathR ,"{}_{}R.png".format(leter,img_coutner)), right_part)
    cv2.imwrite(os.path.join(pathL ,"{}_{}L.png".format(leter,img_coutner)), left_part)
    return

cam = cv2.VideoCapture(1)
print(type(cam))


img_coutner = 0

strt_period = 3

strt_time = time.time()

frames_per_second = 6

fps = 1/frames_per_second

last_frame = strt_time

alphabet2 = "012345"
alphabet = []
for x in alphabet2:
    alphabet.append(str(x))

if True:
    path = "C:/Users/polgo/Desktop/Tiny Test/Right/"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(path)
       print("Right created!")
    path = "C:/Users/polgo/Desktop/Tiny Test/Left/"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(path)
       print("Left created!")

for leter in alphabet:
    path = "C:/Users/polgo/Desktop/Tiny Test/Right/{}".format(leter)
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(path)
       print("{}R created!".format(leter))
    path = "C:/Users/polgo/Desktop/Tiny Test/Left/{}".format(leter)
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(path)
       print("{}L created!".format(leter))

recordingImages = 600
secondsPerFrame = 1
recordingPeriod = recordingImages*secondsPerFrame
preparationTime=20

leter = detectKeyPress()
while True:


    current_time = time.time()
    leter = detectKeyPress()
    if leter == "º":
        leter = "start"
    if leter:

        img_coutner = 0
        winsound.Beep(1500  , 70 )
        start_time = current_time


        while current_time<start_time+preparationTime+recordingPeriod:
            ret,frame = cam.read()
            if not ret:
                print("Failed")
                break

            if  current_time> start_time+preparationTime:  
                winsound.Beep(2250  , 70)
                saveImage(img_coutner,leter,frame)
                img_coutner += 1
                time.sleep(secondsPerFrame)
            else:
                winsound.Beep(500,30)

            current_time = time.time()
            
        winsound.Beep(2500  , 70)
        print("end")
        print(leter)
        leter = ""









print("stoped")
cam.release()

cam.destroyAllWindows()




