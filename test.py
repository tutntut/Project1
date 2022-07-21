import cv2
import numpy as numpy

def tracking():
    cap = cv2.VideoCapture(0)
    cap.set(3,320)
    cap.set(4,240)

    while True:
        ret, frame = cap.read()

        cv2.imshow('video', frame)

        if cv2.waitKey(1)& 0xff == ord('q'):
            break

    cv2.destroyAllwindosws()


tracking()
