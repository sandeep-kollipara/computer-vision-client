#!usr/bin/python3
#https://stackoverflow.com/questions/54949143/opencv-unable-to-read-video-from-mjpeg-stream
import os
import sys
import cv2

IP_ADDRESS = 'cam.sandy.plus'



if __name__ == '__main__':
    
    # Open a URL stream
    stream = cv2.VideoCapture('http://{}/stream.mjpg'.format(IP_ADDRESS))
    while ( stream.isOpened() ):
        # Read a frame from the stream
        ret, img = stream.read()
        cv2.waitKey(35)
        if ret: # ret == True if stream.read() was successful
            cv2.imshow('Video Stream Monitor', img)
    
    input("Press ENTER to exit.")
