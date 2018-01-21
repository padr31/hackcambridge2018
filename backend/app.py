#!flask/bin/python
from time import time
from flask import Flask, send_file, request
import json

from AzureClient import AzureClient
import webcam
import compute
from ImageDrawer import ImageDrawer
from TimeMachine import TimeMachine
from threading import Thread

EMOTIONS = ["anger", "contempt", "disgust", "fear", "happiness", "neutral", "sadness", "surprise"]
FILENAME = 'image.jpg'
FILENAME2 = 'image_s.jpg'
DEBUG = False
MULTITHREADING = False
COLORS = {
    'anger': '#934451',
    'contempt': '#ffe6ae',
    'disgust': '#5e6409',
    'fear': '#d7dae0',
    'happiness': '#ff0080',
    'neutral': '#d7dae0',
    'sadness': '#707784',
    'surprise': '#aa94d0'
}
CURRENT_SUGGESTION = compute.get_suggestion()

app = Flask(__name__, static_url_path='')
client = AzureClient()
id = ImageDrawer()

h_ts = []
h_is = []
h_ds = []
history = []

@app.route('/')
def index():
    return "Nothing here :)"

@app.route('/process')
def process():
    tm = TimeMachine()
    tm.start()
    print("Process started")

    CURRENT_SUGGESTION = compute.get_suggestion()

    # ===== Getting data =====

    take_photo = request.args.get('photo', default="1") == "1"
    file = request.args.get('file', default=FILENAME)

    if file != FILENAME:
        webcam.compress(file, file + "_.jpg")
        file = file + "_.jpg"

    if take_photo:
        if MULTITHREADING:
            thread = Thread(target=webcam.takeImage2, args=(FILENAME, tm))
            thread.start()
        else:
            webcam.takeImage2(FILENAME, tm)

    print(file)
    recognized = client.process_image(file)
    if recognized is None:
        recognized = []
        print("Azure returned None")
    recognized.sort(key=lambda p: p["faceRectangle"]["left"])
    tm.measure("Request")

    #if DEBUG:
    id.write_image(file, recognized, FILENAME2)
    interest = compute.compute(recognized)
    if (interest == 0) and (len(h_is) >= 1):
        interest = h_is[-1]
    tm.measure("Compute")

    if MULTITHREADING and take_photo:
        thread.join()

    print(tm)
    duration = tm.duration()

    # ===== Store timeframe =====

    h_ts.append(tm.st)
    h_is.append(interest)
    h_ds.append(duration)
    history.append(recognized)

    # ===== Postprocessing =====

    isa = h_is
    for i in range(len(isa)):
        current = isa[i]
        if i > 0:
            past = isa[i-1]
            diff = max(past - current - 0.1, 0)
            isa[i] += diff * 0.4

    histogram_frames = history[-4:]
    histogram_data = [
        sum(sum(person["scores"][emotion] for person in obj) for obj in histogram_frames) / len(histogram_frames)
                    for emotion in EMOTIONS
    ]

    status = compute.status(history)

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
        "isa": isa,
        "histogram": histogram_data,
        "histogram_labels": EMOTIONS,
        "status": status,
        "status_color": COLORS[status],
        "suggestion": CURRENT_SUGGESTION
    }
    return json.dumps(response)

@app.route('/last_image.jpg')
def send_image():
    return send_file("image_s.jpg")

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
