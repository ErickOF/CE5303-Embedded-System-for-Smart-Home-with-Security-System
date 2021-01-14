import cv2
import numpy as np
import os


# Add here the names of the people to recognize
NAMES: list = ["None", "Erick"]
HAARCASCADE_FRONTALFACE: str = "haarcascade_frontalface_default.xml"


def recognizeFacePlot() -> None:
    """This function is used as a test in the workstation.
    """
    # Initialize id counter
    _id: int = 0

    # Create recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Load training data
    recognizer.read("training.yml")

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades
                                        + HAARCASCADE_FRONTALFACE)

    font = cv2.FONT_HERSHEY_SIMPLEX

    # Open camera
    cam: cv2.VideoCapture = cv2.VideoCapture(0)
    # Set video width and height
    cam.set(3, 640)
    cam.set(4, 480)

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        # Take a photo
        ret, img = cam.read()

        if ret:
            # Convert to gray scale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            # Draw faces
            for(x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Recognize face
                _id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

                # Check if confidence is less than 100
                # 0 is perfect match
                if (confidence < 100):
                    _id = NAMES[_id]
                else:
                    _id = "unknown"

                confidence = f"  {round(100 - confidence)}%"

                cv2.putText(img, str(_id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(confidence), (x + 5, y + h - 5),
                            font, 1, (255, 255, 0), 1)

                cv2.imshow("Camera", img)

        # Press "ESC" for exiting video
        key = cv2.waitKey(10) & 0xff

        if key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


def recognizeFace(img: np.array) -> None:
    """This function must be called by the API.
    """
    # Initialize id counter
    _id: int = 0

    # Create recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Load training data
    recognizer.read("training.yml")

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


if __name__ == "__main__":
    #recognizeFacePlot()

    # Open camera
    cam: cv2.VideoCapture = cv2.VideoCapture(0)
    # Set video width and height
    cam.set(3, 640)
    cam.set(4, 480)

    img = None

    ret = False

    while not ret:
        # Take a photo
        ret, img = cam.read()

    print(img.shape)
    print(recognizeFace(img))
