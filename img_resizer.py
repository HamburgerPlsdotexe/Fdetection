# from PIL import Image as img
# import os as os
# import cv2

# img_root = r"C:\\Users\\cagla\\source\\repos\\Fdetection\\images"

# def resize():  
#     """Using PIL as image editing lib""" 
#     for subdir, dirs, files in os.walk(img_root):
#         img_count = 0
#         for filename in files:
#             filepath = subdir + os.sep + filename
#             image = img.open(filepath)      
#             if(image.size != (1280,720)):
#                 if not (filename[0].isdigit()):
#                     image.resize((1280,720))
#                     new_image = image.save(subdir + '\\' + str(img_count) + ".jpg")
#                     img_count += 1
#                     print(img_count)
#                     os.remove(filepath)

# def resizeCV():
#     """Using OpenCV as image editing lib"""
#     for subdir, dirs, files in os.walk(img_root):
#         img_count = 0
#         for filename in files:
#             filepath = subdir + os.sep + filename
#             image = cv2.imread(filepath)
#             print(image.shape, subdir)
#             if(image.shape != (720, 1280, 3)):
#                 if not (filename[0].isdigit()):
#                     resized = cv2.resize(image, (1280, 720))
#                     cv2.imwrite(subdir + '\\' + str(img_count) + ".jpg", resized)
#                     img_count += 1
#                     os.remove(filepath)    

                



# resizeCV()