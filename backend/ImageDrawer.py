from AzureClient import AzureClient
import operator
import numpy as np
import cv2
import matplotlib.pyplot as plt

class ImageDrawer:

    def __init__(self):
        self.ac = AzureClient()

    def renderResultOnImage(self, result, img):
        for currFace in result:
            faceRectangle = currFace['faceRectangle']
            cv2.rectangle( img,(faceRectangle['left'],faceRectangle['top']),
                               (faceRectangle['left']+faceRectangle['width'], faceRectangle['top'] + faceRectangle['height']),
                           color = (255,0,0), thickness = 5 )
        for currFace in result:
            faceRectangle = currFace['faceRectangle']
            currEmotion = max(currFace['scores'].items(), key=operator.itemgetter(1))[0]
            textToWrite = "%s" % ( currEmotion )
            cv2.putText( img, textToWrite, (faceRectangle['left'],faceRectangle['top']-10), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,0,0), 1 )

    def draw_image(self, image_path):

        with open( image_path, 'rb' ) as f:
            data = f.read()

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self.ac.key
        headers['Content-Type'] = 'application/octet-stream'
        json = None
        params = None
        result = self.ac.process_request( json, data, headers, params )

        if result is not None:
            # Load the original image from disk
            data8uint = np.fromstring(data, np.uint8)  # Convert string to an unsigned int array
            img = cv2.cvtColor(cv2.imdecode(data8uint, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)

            self.renderResultOnImage(result, img)

            ig, ax = plt.subplots(figsize=(15, 20))
            ax.imshow(img)
            plt.savefig('faces_detected.png')

# sample use
#
# now in this directory, you will find an annotated photo
# id = ImageDrawer()
# id.draw_image('/Users/markopuza/Downloads/IMG_20180120_131159.jpg')
