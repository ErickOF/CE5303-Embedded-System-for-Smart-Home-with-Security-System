import cv2
import os


HAARCASCADE_FRONTALFACE: str = "haarcascade_frontalface_default.xml"
MAX_SAMPLES: int = 30


def takeSamples() -> None:
    """
    This function takes the photos of the new person.
    """
    # Open camera
    cam: cv2.VideoCapture = cv2.VideoCapture(0)
    # Set video width and height
    cam.set(3, 640)
    cam.set(4, 480)

    # Create the haar cascade classifier
    faceDetector: cv2.CascadeClassifier = cv2.CascadeClassifier(cv2.data.haarcascades
                                                                + HAARCASCADE_FRONTALFACE)

    username: str = input("User name: ")

    print("\nInitializing face capture...")

    # Initialize individual sampling face count
    count: int = 0

    while count < 30:
        # Take photo
        ret, img = cam.read()
        # Flip video image vertically
        img = cv2.flip(img, -1)
        # To gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = faceDetector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite(f"dataset/{username}{count}.jpg", gray[y:y+h, x:x+w])
            cv2.imshow("Image", img)

        # Press "ESC" for exiting
        #key = cv2.waitKey(100)

        # if key == 27:
        #    count = 30

    cam.release()
    cv2.destroyAllWindows()
    print("\nFinished...")


if __name__ == "__main__":
    takeSamples()
