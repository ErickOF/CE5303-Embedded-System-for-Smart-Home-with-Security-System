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
    _ids: list = []

    users: int = 1
    names: dict = {'None': 0}

    for imagePath in imagePaths:
        # Convert to grayscale
        img: np.array = np.array(Image.open(imagePath).convert("L"))

        # Get image name, id
        name, _id = os.path.split(imagePath)[-1].split("_")

        # Get detected face
        faces = detector.detectMultiScale(img)

        # Add faces
        for (x, y, w, h) in faces:
            faceSamples.append(img[y:y+h, x:x+w])
            _ids.append(int(_id.split(".")[0]))

            if name not in names:
                names[name] = users
                users += 1
            
            labels.append(names[name])

    print(names)

    return faceSamples, labels, _ids


def train() -> None:
    """
    This function trains the model.
    """
    print("Training faces... Wait...")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Get faces, labels, ids
    faces, labels, _ids = readImgs(PATH)
    # Recognize face
    recognizer.train(faces, np.array(labels))

    # Save the model
    recognizer.write("training.yml")

    print(f"\n{len(np.unique(_ids))} faces trained.")


if __name__ == "__main__":
    train()
