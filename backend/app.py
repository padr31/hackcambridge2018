#!flask/bin/python
from flask import Flask
from AzureClient import AzureClient
import webcam

FILENAME = '/Users/michal/Desktop/pictures'

app = Flask(__name__)
client = AzureClient()


@app.route('/')
def index():
    webcam.takeImage(FILENAME)
    response = client.process_image(FILENAME)
    return response


if __name__ == '__main__':
    app.run(debug=True)
