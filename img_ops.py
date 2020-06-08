import cv2
import os
import numpy as np
import PIL as pil
from main import cascPath
from main import face_cascade
from PIL import Image as img

img_root = r"C:\\Users\\cagla\\source\\repos\\Fdetection\\images"
dirs = os.listdir(img_root)
individuals = ["", "Dad", "Cağlar"]

def resize():   
    """Using OpenCV as the image editing lib"""
    for subdir, dirs, files in os.walk(img_root):
        img_count = 0
        for filename in files:
            filepath = subdir + os.sep + filename
            image = cv2.imread(filepath)
            if not (filename[0].isdigit()):
                if(image.shape != (720, 1280, 3)):
                    resized = cv2.resize(image, (1280, 720))
                    cv2.imwrite(subdir + '\\' + str(img_count) + ".jpg", resized)
                    img_count += 1
                    os.remove(filepath)


def detect_face(img):
    """ Function for detecting faces from still images"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if (len(faces) == 0):
        return None, None

    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]   


def img_operations():
    """ Function that heavily works with system calls. Gets image filenames and images alltogether and works with OpenCV to get actual data"""
    resize()
    faces =     []
    labels =    []
    while True:
        for dir in dirs:
            if not dir.startswith("S"):
                continue
            label = int(dir.replace("S", ""))
            individuals_path = img_root + "/" + dir
            individual_img_name = os.listdir(individuals_path)

            for image_name in individual_img_name:
                # Ignore system files
                if image_name.startswith("."):
                    continue 
                
                img_path = individuals_path + "/" + image_name
                img = cv2.imread(img_path)
                cv2.imshow("Training on image...", img)
                cv2.waitKey(100)
                
                # Detect the face inside the picture
                face, rect = detect_face(img)

                if face is not None:                    
                    faces.append(face)
                    labels.append(label)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        SystemExit(0)
                    cv2.destroyAllWindows()
                    cv2.waitKey(1)
                    cv2.destroyAllWindows()
        return faces, labels            
            

print("Preparing data...")
faces, labels = img_operations()
print("Data prepared")

#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

recognizer=cv2.face.EigenFaceRecognizer_create()
recognizer.train(faces, np.array(labels))