import cv2
import sys
import numpy as np
import os as os
import threading as th

cascPath = r"C:\\Users\\cagla\\source\\repos\\Fdetection\\data\\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascPath)

# video_capture = cv2.VideoCapture(0)



# def img_operations():
#     """ Function that heavily works with system calls. Gets image filenames and images alltogether"""
#     while True:
#         img_root = r"C:\\Users\\cagla\\source\\repos\\Fdetection\\images"
#         dirs = os.listdir(img_root)
#         print(dirs)
#         for dir in dirs:
#             if not dir.startswith("S"):
#                 continue
#             label = int(dir.replace("S", ""))
#             individuals_path = img_root + "/" + dir
#             individual_img_name = os.listdir(individuals_path)

#             for image_name in individual_img_name:
#                 # Ignore system files
#                 if image_name.startswith("."):
#                     continue 
                
#                 img_path = individuals_path + "/" + image_name
#                 image = cv2.imread(img_path)
#                 cv2.imshow("Training on image...", image)
#                 cv2.waitKey(100)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# # Thread creation and start in order to balance the workload
# img_thread = th.Thread(target=img_operations)
# start_thread = True

# while True:
#     # Capture frame-by-frame
#     _, frame = video_capture.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )

#     # Draw a rectangle around the faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         cv2.putText(frame, "nieger" , (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,  0.65, (50,170,50), 2)   

#     # Starting the img_thread
#     if start_thread:
#         img_thread.start()
#         start_thread = False
            
#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything is done, release the capture
# img_thread.join()
# video_capture.release()
# cv2.destroyAllWindows()