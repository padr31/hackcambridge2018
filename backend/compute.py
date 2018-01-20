import json
import math

def compute(o):
    # print(o)
    vals = [evalPerson(p) for p in o]
    avg = sum(vals) / len(vals)
    print("Average: " + str(avg))


def evalPerson(p):
    s = p['scores']
    r = p['faceRectangle']
    print(s)

    interest = s['happiness'] ** 2 \
           - s['sadness'] ** 2 \
           - s['neutral'] ** 2 \
           + s['surprise'] ** 2 \
           + s['fear'] ** 2 \
           + s['contempt'] ** 2 \
           - s['disgust'] ** 2 \
           - s['anger'] ** 2
    area = r['width'] * r['height']
    weight = 1 - math.exp(-area)

    return interest * weight
