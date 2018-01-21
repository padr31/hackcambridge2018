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

    exP = 1/1.2
    exN = 1/exP

    interest = s['happiness'] ** exP \
           + s['surprise'] ** exP \
           + s['fear'] ** exP \
           + s['contempt'] ** exP \
           - s['sadness'] ** exN \
           - s['disgust'] ** exN \
           - s['anger'] ** exN \
           - math.exp((s['neutral'] - 1)*4)
    area = r['width'] * r['height'] / float(4608 * 3456)
    relative_width = math.sqrt(r['width'] * r['height'] / float(4608 * 3456))
    #weight = (1 - math.exp(-area * 234)) * (1 - s["neutral"] / 2)
    weight = relative_width * (1 - s["neutral"] / 2)

    p["weight"] = weight
    p["interest"] = interest
    p["relative_width"] = relative_width

    return (interest, weight)
