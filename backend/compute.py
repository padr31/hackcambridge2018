import json
import math

def compute(o):
    # print(o)
    vals = [evalPerson(p) for p in o]
    if len(vals) == 0: return 0

    weights_sum = sum(weight for (interest, weight) in vals)
    vals = [(interest, weight / weights_sum) for (interest, weight) in vals]

    for i in range(len(o)):
        o[i]["weight_normalized"] = vals[i][1]

    avg = sum(interest * weight for (interest, weight) in vals)
    return avg

def evalPerson(p):
    s = p['scores']
    r = p['faceRectangle']
    #print(s)

    exP = 1/2
    exN = 1/exP

    interest = 1 - math.exp(- s['happiness'] * 5)
           #+ s['surprise'] ** exP \
           #+ s['fear'] ** exP \
           #+ s['contempt'] ** exP \
           #- s['sadness'] ** exN \
           #- s['disgust'] ** exN \
           #- s['anger'] ** exN \
           #- math.exp((s['neutral'] - 1)*4)
    area = r['width'] * r['height'] / float(4608 * 3456)
    relative_width = math.sqrt(r['width'] * r['height'] / float(4608 * 3456))
    #weight = (1 - math.exp(-area * 234)) * (1 - s["neutral"] / 2)
    weight = relative_width * (1 - s["neutral"] / 2)

    p["weight"] = weight
    p["interest"] = interest
    p["relative_width"] = relative_width

    return (interest, weight)

def status(history):
    if len(history) == 0:
        return 'neutral'
    feelings =  _averageFrames(history)
    return max((sum(f[k] for f in feelings), k) for k,v in feelings[0].items())[1]


def _averageFrames(history):
    return list(map(lambda frame: average(frame)), history)


def average(frame):
    feeling = {
        'anger': 0,
        'contempt': 0,
        'disgust': 0,
        'fear': 0,
        'happiness': 0,
        'neutral': 0,
        'sadness': 0,
        'surprise': 0
    }

    for person in frame:
        for k,v in person['scores'].items():
            feeling[k] += v

    for k, v in feeling.items():
        feeling[k] /= len(frame)

    return feeling
