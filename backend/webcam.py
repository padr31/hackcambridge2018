
# from cv2 import *
#
# def capture():
#     # initialize the camera
#     cam = VideoCapture(1)  # 0 -> index of camera
#     s, img = cam.read()
#     if s:  # frame captured without any errors
#         #namedWindow("cam-test", CV_WINDOW_AUTOSIZE)
#         #imshow("cam-test", img)
#         #waitKey(0)
#         #destroyWindow("cam-test")
#         imwrite("filename.jpg", img)  # save image
#     else:
#         print("problem")

import urllib.request

def takeImage(filename):
    url = "http://localhost:4747/cam/1/frame.jpg"
    urllib.request.urlretrieve(url, filename)
