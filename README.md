# VR-Keyboard-Project
This is the place where I put all the code for the VR keyboard Project, feel free to download it and try it out




IMPORTANT NOTES:
-------------------------------------------------------------------------------------------------------------------------------------------------

If you want to use the code, you will need to change the following:

Controller.py ----- Line 31, cam = cv2.VideoCapture(1) ------- Change the value 1 to (0 for default camera, 1 [or other numbers] for other cameras)
-------------------------------------------------------------------------------------------------------------------------------------------------

If you want to see the hand signs for each letter, go to the Evaluation.py file:
- left hand is heigh (top 0, bottom 5)
- right hand is verticality (left 0, right 5)

-------------------------------------------------------------------------------------------------------------------------------------------------
To run the program, you can either run Controller.py so that the program executes normaly or you can run game.py for a small and fun game to test your skills (it requires inputs, so run it in idle or smthign like it)

-------------------------------------------------------------------------------------------------------------------------------------------------

Change at your own risk

NEVER CHANGE THE 5 5 VALUE of the Evaluation.py matrix, that is the default value for when no sign is detected, changing that will make it so that it activates everytime exept when a sign is detected 

-------------------------------------------------------------------------------------------------------------------------------------------------