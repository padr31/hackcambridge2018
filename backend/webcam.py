
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
import os
import time

def takeImage(filename):
    url = "http://localhost:4747/cam/1/frame.jpg"
    urllib.request.urlretrieve(url, filename)

def ex(command, p=True):
    process = os.popen(command)
    output = process.read()
    process.close()
    return output

def takeImage2(filename):
    adb = "%userprofile%\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb "
    dcim = "/storage/emulated/0/DCIM/Camera/"

    ex(adb + 'shell input keyevent 27')
    time.sleep(2)

    files = ex(adb + 'shell ls ' + dcim).strip().split("\n")
    file = files[-1]
    print(file)

    ex(adb + 'pull ' + dcim + file + ' .', p=False)
    ex(adb + 'shell rm ' + dcim + file)
    os.remove(filename) if os.path.exists(filename) else None
    os.rename(file, filename)

if __name__ == '__main__':
    takeImage2("image.jpg")
