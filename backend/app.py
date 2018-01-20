#!flask/bin/python
from flask import Flask
from AzureClient import AzureClient
import webcam
import compute
from ImageDrawer import ImageDrawer

FILENAME = 'image.jpg'
FILENAME2 = 'image_s.jpg'

app = Flask(__name__)
client = AzureClient()
id = ImageDrawer()

@app.route('/')
def index():
    webcam.takeImage2(FILENAME)
    response = client.process_image(FILENAME)
    id.write_image(FILENAME, response, FILENAME2)
    compute.compute(response)
    return response

if __name__ == '__main__':
    #app.run(debug=True)
    index()
