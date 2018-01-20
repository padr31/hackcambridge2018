#!flask/bin/python
from time import time
from flask import Flask, send_file
import json

from AzureClient import AzureClient
import webcam
import compute
from ImageDrawer import ImageDrawer
from TimeMachine import TimeMachine

FILENAME = 'image.jpg'
FILENAME2 = 'image_s.jpg'

app = Flask(__name__, static_url_path='')
client = AzureClient()
id = ImageDrawer()

h_ts = []
h_is = []
h_ds = []

@app.route('/')
def index():
    return "Nothing here :)"

@app.route('/process')
def process():
    tm = TimeMachine()
    tm.start()
    print("Process started")

    webcam.takeImage2(FILENAME, tm)
    recognized = client.process_image(FILENAME)
    tm.measure("Request")
    #id.write_image(FILENAME, recognized, FILENAME2)
    interest = compute.compute(recognized)
    tm.measure("Compute")

    print(tm)
    duration = tm.duration()

    h_ts.append(tm.st)
    h_is.append(interest)
    h_ds.append(duration)

    response = {
        "time": tm.st,
        "interest": interest,
        "duration": duration,
        "people": len(recognized),
        "tm": str(tm),
        "debug": recognized,
        "ts": h_ts,
        "is": h_is,
        "ds": h_ds,
    }
    return json.dumps(response)

@app.route('/last_image.jpg')
def send_image():
    return send_file("image.jpg")

@app.route('/img')
def randomimg():
    return "https://vignette.wikia.nocookie.net/austinally/images/1/14/Random_picture_of_shark.png/revision/latest?cb=20150911004230"

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
    #index()
