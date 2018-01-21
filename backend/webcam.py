
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
from threading import Thread

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
    time.sleep(.6+.2)
    tm.measure("Photo taken")

    # Get filename
    files = ex(adb + 'shell ls ' + dcim).strip().split("\n")
    file = files[-1]

    # Pull and remove from device
    ex(adb + 'pull ' + dcim + file + ' tmp', p=False)
    tm.measure("Pull")

    def remove(cmd):
        ex(cmd)
        tm.measure("Remove")
    thread = Thread(target=remove, args=(adb + 'shell rm ' + dcim + file,))
    thread.start()

    compress("tmp/" + file, filename)
    tm.measure("Compress")

    thread.join()

    # Remove temp file
    #os.remove("tmp/" + file)
    #tm.measure("Remove")

def compress(input, output):
    # Compress
    picture = Image.open(input)
    os.remove(output) if os.path.exists(output) else None
    picture.save(output, "JPEG", optimize=True, quality=20)


#if __name__ == '__main__':
#    takeImage2("image.jpg")
