
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
from PIL import Image

def takeImage(filename):
    url = "http://localhost:4747/cam/1/frame.jpg"
    urllib.request.urlretrieve(url, filename)

def ex(command, p=True):
    process = os.popen(command)
    output = process.read()
    process.close()
    return output

def takeImage2(filename, tm):
    adb = "%userprofile%\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb "
    dcim = "/storage/emulated/0/DCIM/Camera/"

    # Take photo
    ex(adb + 'shell input keyevent 27')
    time.sleep(.6+.1)
    tm.measure("Photo taken")

    # Get filename
    files = ex(adb + 'shell ls ' + dcim).strip().split("\n")
    file = files[-1]

    # Pull and remove from device
    ex(adb + 'pull ' + dcim + file + ' .', p=False)
    tm.measure("Pull")
    ex(adb + 'shell rm ' + dcim + file)
    tm.measure("Remove")

    # Compress
    picture = Image.open(file)
    os.remove(filename) if os.path.exists(filename) else None
    picture.save(filename, "JPEG", optimize=True, quality=50)
    tm.measure("Compress")

    # Remove temp file
    os.remove(file)
    tm.measure("Remove")

#if __name__ == '__main__':
#    takeImage2("image.jpg")
