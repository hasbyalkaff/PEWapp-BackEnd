from flask import Flask, request, jsonify
from PIL import Image
import io
import base64

from myClass.Landmark import Landmark
from myClass.Feature import Feature
from myClass.Classifier import Classifier
from myClass.FaceExpression import FaceExpression

app = Flask(__name__)
lmk_ntrl = None

def cetak(lmk):
    for i, value in enumerate(lmk):
        print(f"{value.x} - {value.y}")

def extract_feature(feature):
    tamp = []
    for (label, value) in feature.items():
        tamp.append(value)
    return tamp

@app.route("/testing", methods=['POST'])
def test():
    post_image = request.json['image']
    post_step = request.json['step']
    image_base64 = base64.b64decode(post_image)
    image = Image.open(io.BytesIO(image_base64))
    image.save("result.jpeg")
    expression = "Kosong"

    myLandmark = Landmark("result.jpeg")
    lmk = myLandmark.get_landmark()

    global lmk_ntrl
    if post_step == 0: # netral
        lmk_ntrl = lmk

    elif lmk_ntrl == None:
        print(expression)

    elif post_step == 1: # peak
        lmk_peak = lmk
        myFeature = Feature()
        myFeature.calculation_expression(lmk_ntrl, lmk_peak)
        feature = myFeature.get_feature_expression()
        feature = extract_feature(feature)

        myClassifier = Classifier("exp", 1)
        result = myClassifier.check(feature)

        myExpression = FaceExpression()
        expression = myExpression.get_expression(result)

    return jsonify({"expression":expression})

@app.route("/training", methods=['GET'])
def train():
    return "Hello Training"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")