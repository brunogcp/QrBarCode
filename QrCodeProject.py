import cv2
import numpy as np
from pyzbar.pyzbar import decode

URL = 'http://192.168.1.101:8080'
vs = cv2.VideoCapture(URL + "/video")

with open('myDataFile.txt') as file:
    myDataList = file.read().splitlines()

while True:
    ret, frame = vs.read()
    if not ret:
        continue
    for barcode in decode(frame):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(frame, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
