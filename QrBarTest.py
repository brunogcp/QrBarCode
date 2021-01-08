import cv2
import numpy as np
from pyzbar.pyzbar import decode

URL = 'http://192.168.1.101:8080'
vs = cv2.VideoCapture(URL + "/video")

# img = cv2.imread('img.png')
# vid = cv2.VideoCapture(0)
# vid.set(3, 640)
# vid.set(4, 480)

while True:
    # success, img = vid.read()
    # img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
    # img = cv2.imdecode(img_arr, -1)
    ret, frame = vs.read()
    if not ret:
        continue
    for barcode in decode(frame):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(frame, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
