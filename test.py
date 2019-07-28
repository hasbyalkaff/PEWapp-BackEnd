from myClass.Landmark import Landmark
from myClass.Feature import Feature
from myClass.Classifier import Classifier

def cetak(lmk):
    for i, value in enumerate(lmk):
        print(f"{value.x} - {value.y}")

def extract_feature(feature):
    tamp = []
    for (label, value) in feature.items():
        tamp.append(value)
    return tamp
        
myLandmark = Landmark("S087_002_00000020.png")
landmark = myLandmark.get_landmark()
cetak(landmark)

myFeature = Feature()
myFeature.calculation_netral(landmark)
feature = myFeature.get_feature_netral()
print(feature)

feature = extract_feature(feature)
print(feature)

# myClassifier = Classifier("netral", 1)
# myClassifier.check(feature)