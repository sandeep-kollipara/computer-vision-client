#!usr/bin/python3
import os
import sys
import struct
import pickle
import imutils
import socket
import cv2



if __name__ == '__main__':

    # Client socket
    # create an INET, STREAMing socket : 
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_ip = 'socket.sandy.plus' #'<localhost>'# Standard loopback interface address (localhost)
    port = 10050 # Port to listen on (non-privileged ports are > 1023)
    # now connect to the web server on the specified port number
    client_socket.connect((host_ip,port)) 
    #'b' or 'B'produces an instance of the bytes type instead of the str type
    #used in handling binary data from network connections
    data = b""
    # Q: unsigned long long integer(8 bytes)
    payload_size = struct.calcsize("Q")
    '''
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4*1024)
            if not packet: break
            data+=packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
        while len(data) < msg_size:
            data += client_socket.recv(4*1024)
        frame_data = data[:msg_size]
        data  = data[msg_size:]
        frame = pickle.loads(frame_data)
        cv2.imshow("Receiving...",frame)
        key = cv2.waitKey(10) 
        if key  == 13:
            break
    client_socket.close()
    '''
    
    s = client_socket
    s.connect((host, port))
    while True: 
        try:
            print("From Server: ", s.recv(1024)) 
            s.send(raw_input("Client please type: "))
        except:
            break
    s.close()
    
    input("Press ENTER to exit.")
    print("Bye!")
