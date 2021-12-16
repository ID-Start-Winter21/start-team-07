__author__  = "Michael Eggers"
__license__ = "MIT"

import cv2
import face_recognition as fr
import numpy as np
from werkzeug.datastructures import UpdateDictMixin

videoCapture = None

def startCamera():
    global videoCapture
    videoCapture = cv2.VideoCapture(0)

def stopCamera():
    videoCapture.release()


def generateEncodings(names: list, filenames: list):
    names2encodings = []
    for name, file in zip(names, filenames):
        pic = fr.load_image_file(file)
        enc = fr.face_encodings(pic)
        names2encodings.append((name, enc))

    return names2encodings

def recognizeFaceForEncoding(name2encoding):
    ret, frame = videoCapture.read()
    smallFrame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    faceLocations = fr.face_locations(smallFrame)

    for faceLocation in faceLocations:
        # faceLocation = np.asarray(faceLocation)
        # p1 = (faceLocation[3], faceLocation[2])
        # p2 = (faceLocation[1], faceLocation[0])

        unknownEncodings = fr.face_encodings(smallFrame)
        for unknownEncoding in unknownEncodings:
            if fr.compare_faces(name2encoding[1], unknownEncoding)[0]:
                return name2encoding
        
    return None
