from myClass.Landmark import Landmark
from myClass.Feature import Feature
from myClass.Classifier import Classifier
import os

url = "assets/dataset"
expression = {
        "sedih"    : 1,
        "senang"   : 2,
        "terkejut" : 3
}
current = "exp"
training = []
target = []

def cetak(lmk):
        for i, value in enumerate(lmk):
                print(f"{value.x} - {value.y}")

def extract_feature(feature):
        tamp = []
        for (label, value) in feature.items():
                tamp.append(value)
        return tamp

def get_feature(path_to_netral, path_to_peak):
        myLandmark = Landmark(path_to_netral)
        lmk_netral = myLandmark.get_landmark()
        # cetak(lmk_netral)
        
        myLandmark = Landmark(path_to_peak)
        lmk_peak = myLandmark.get_landmark()
        # cetak(lmk_peak)

        myFeature = Feature()
        myFeature.calculation_expression(lmk_netral, lmk_peak)
        feature = myFeature.get_feature_expression()
        # print(feature)
        return(feature)

people = os.listdir(url)
sum_people = len(people)
num = 0
for person in people:
        percent = (num/sum_people) * 100
        print(f"({percent:6.2f}) - {person}", end="\r")
        for exp, tar in expression.items():
                path = url + "/" + person + "/" + exp
                if os.path.isdir(path):
                        idx_netral, idx_peak = 0, -1
                        image = os.listdir(path)
                        
                        while not image[idx_netral].endswith('.png'):
                                idx_netral += 1
                        while not image[idx_peak].endswith('.png'):
                                idx_peak -= 1
                        
                        # print(image[idx_netral])
                        # print(image[idx_peak])
                        path_netral = path + "/" + image[idx_netral]
                        path_peak = path + "/" + image[idx_peak]
                        feature = get_feature(path_netral, path_peak)

                        feature = extract_feature(feature)
                        training.append(feature)
                        target.append(tar)
        num += 1
        print(f"( DONE ) - {person}")
print()

myClassifier = Classifier(current, 0)
myClassifier.fit(training, target)
myClassifier.create_model()