import cv2
import numpy as np
from PIL import Image
import os


HAARCASCADE_FRONTALFACE: str = "haarcascade_frontalface_default.xml"
PATH: str = "dataset"


def readImgs(path: str) -> tuple:
    """
    This function reads all images and returns them with their labels.

    Params
    ------------------------------------------------------------------
        path: str.
            Path to the folder.
    """
    detector: cv2.CascadeClassifier = cv2.CascadeClassifier(cv2.data.haarcascades
                                                            + HAARCASCADE_FRONTALFACE)
    # Get all paths to the image
    imagePaths: list = [os.path.join(path, file) for file in os.listdir(path)]
    faceSamples: list = []
    labels: list = []

    for imagePath in imagePaths:
        # Convert to grayscale
        img: np.array = np.array(Image.open(imagePath).convert("L"))

        # Get image id
        _id = int(os.path.split(imagePath)[-1].split(".")[1])
        # Get detected face
        faces = detector.detectMultiScale(img)

        # Add faces
        for (x, y, w, h) in faces:
            faceSamples.append(img[y:y+h, x:x+w])
            labels.append(_id)

    return faceSamples, labels


def train() -> None:
    """
    This function trains the model.
    """
    print("Training faces... Wait...")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Get faces and labels
    faces, labels = readImgs(PATH)
    # Recognize face
    recognizer.train(faces, np.array(labels))

    # Save the model
    recognizer.write("training.yml")

    print(f"\n{len(np.unique(labels))} faces trained.")


if __name__ == "__main__":
    train()
