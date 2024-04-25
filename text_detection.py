#!usr/bin/python3
#https://nanonets.com/blog/ocr-with-tesseract/
import os
import sys
import cv2
import time

IP_ADDRESS = 'cam.sandy.plus'



if __name__ == '__main__':
    
    video = cv2.VideoCapture("http://{}/stream.mjpg".format(IP_ADDRESS))
    
    while True:
        status, frame = video.read()
        cv2.imwrite("images/ocr_transfer.jpg", frame)
        sys.argv = ["ocr_tutorial_nanonetsdotcom.py", "images/ocr_transfer.jpg"]
        with open("ocr_tutorial_nanonetsdotcom.py") as pyfile:
            exec(pyfile.read())
        #waitKey(10000)
        time.sleep(10)
        
    video.release()
    cv2.destroyWindows()
    
    input("Press ENTER to exit.")
