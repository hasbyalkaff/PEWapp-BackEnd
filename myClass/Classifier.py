from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from myClass.Model import Model

class Classifier:
    def __init__(self, type, step):
        self._model = Model(type)
        self._type = type
        if step == 0: #training
            self._clf = SVC()
        else: #testing
            self._clf = self.load_model()

    def fit(self, features, target):
        if self._type == "sedih":
            SVC(C=1.0, gamma='auto', kernel='rbf')
        elif self._type == "senang":
            SVC(C=1.0, gamma='auto', kernel='rbf')
        elif self._type == "terkejut":
            SVC(C=1.0, gamma='auto', kernel='rbf')
        elif self._type == "exp":
            OneVsRestClassifier(SVC(C=1.0, gamma='auto', kernel='rbf'))
        elif self._type == "netral":
            SVC(C=1.0, gamma='auto', kernel='rbf')
        
        self._clf.fit(features, target) 

    def check(self, features):
        return self._clf.predict([features])
    
    def create_model(self):
        self._model.create(self._clf)

    def load_model(self):
        return self._model.get()