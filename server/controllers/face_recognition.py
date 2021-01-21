import cv2
import numpy as np
import os


# Add here the names of the people to recognize
NAMES: list = ["None", "Erick"]
HAARCASCADE_FRONTALFACE: str = "haarcascade_frontalface_default.xml"


def recognizeFace(img: np.array) -> None:
    """This function must be called by the API.
    """
    # Initialize id counter
    _id: int = 0

    # Create recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Load training data
    recognizer.read("../src/training.yml")

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades
                                        + HAARCASCADE_FRONTALFACE)

    # Convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Define min window size to be recognized as a face
    minW = 0.1*gray.shape[0]
    minH = 0.1*gray.shape[1]

    # Detect faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    rectangles: list = []
    recognizedFaces: list = []
    confidences: list = []

    for (x, y, w, h) in faces:
        # Start (x, y), end (x, y)
        rectangles.append([(x, y), (x + w, y + h)])

        # Recognize face
        _id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less than 100
        # 0 is perfect match
        if (confidence < 100):
            recognizedFaces.append(NAMES[_id])
        else:
            recognizedFaces.append("unknown")

        confidences.append(round(100 - confidence, 2))

    return {'rectangles': rectangles, 'faces': recognizedFaces, 'confidences': confidences}

