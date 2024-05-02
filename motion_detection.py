#!usr/bin/python3
#https://github.com/misbah4064/motion_detection
import os
import sys
import cv2
import logging
from datetime import datetime

IP_ADDRESS = 'cam.sandy.plus'
SCREEN_WIDTH = 640 # Can be automated
SCREEN_HEIGHT = 480 # Can be automated



if __name__ == '__main__':
    
    video = cv2.VideoCapture("http://{}/stream.mjpg".format(IP_ADDRESS)) #Shifted to the beginning of the code
    
    image = video.read()[1]
    cv2.imwrite(r"images/background.png", image)
    background = cv2.imread(r"images/background_day.png") #CHange this back to 'background.png' for auto-initialization
    background = cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
    background = cv2.GaussianBlur(background,(21,21),0)
    
    timer = datetime.now().second + 5 # Giving 5 second headstart before logging warnings
    while True:
        status, frame = video.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21,21), 0)
         
        diff = cv2.absdiff(background,gray)
        
        thresh = cv2.threshold(diff,30,255,cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations = 2)
        
        cnts,res = cv2.findContours(thresh.copy(),
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        i = 0
        for contour in cnts:
            if cv2.contourArea(contour) < 10000 :
                 continue
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 3)
            
            if (x+w)/2 < SCREEN_WIDTH/3:
                hori_pos = "Left"
            elif (x+w)/2 > 2*SCREEN_WIDTH/3:
                hori_pos = "Right"
            else:
                hori_pos = "Center"
            if (y+h)/2 < SCREEN_HEIGHT/3:
                vert_pos = "Bottom"
            elif (y+h)/2 > 2*SCREEN_HEIGHT/3:
                vert_pos = "Top"
            else:
                vert_pos = "Middle"
            
            if datetime.now().second == timer:
                logging.warning("[Time:"+datetime.now().strftime("%H:%M:%S")+"]Object #"+str(i+1)+" detected: "+vert_pos+"-"+hori_pos+" Wdt: "+str(w)+"px Hgt "+str(h)+"px.")
            if timer > 60:
                timer = 0
            else:
                timer += 1
            i+=1
            
        cv2.imshow("All Contours",frame)
        
        # cv2.imshow("Threshold Video",thresh)
        
        # cv2.imshow("Diff Video",diff)
        # cv2.imshow("Gray Video",gray)
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        
    video.release()
    cv2.destroyWindows()
    
    input("Press ENTER to exit.")
