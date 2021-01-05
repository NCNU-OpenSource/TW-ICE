import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import DB_CRUD as db
import picamera as pic
import os
def grab_photo():
    #set up camera object
    cap = cv2.VideoCapture(0)

    #QR code detection object
    detector = cv2.QRCodeDetector()

    while True:
        #get the image
        _, frame = cap.read()
        
        #decode image
        decodedObjects = pyzbar.decode(frame)

        #make a list to store data
        data = []
        for obj in decodedObjects:
            data.append(str(obj.data).split("'"))
            print(data[0][1])

            #check if is new data or not
            pic.check_data(data[0][1])
            
            #input data to database
            #db.create_new_data_with_qrcode(data[0][1])

        if len(data) != 0:
            break

    #close the camera
    cap.release()

    #take a photo
    action = "fswebcam --save picture/" + data[0][1] + ".jpg"
    os.system(action)
