from joblib import dump, load

class Model:
	def __init__(self, type):
		url = "assets/model/"
		if type == "sedih":
			self._name = url + "model_sedih.joblib"
		elif type == "senang":
			self._name = url + "model_senang.joblib"
		elif type == "terkejut":
			self._name = url + "model_terkejut.joblib"
		elif type == "exp":
			self._name = url + "model_expression.joblib"
		elif type == "netral":
			self._name = url + "model_netral"

	def create(self, model):
		dump(model, self._name)

	def get(self):
		return load(self._name) 