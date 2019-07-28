class FaceExpression:
	def __init__(self):
		self.netral = 0
		self.sedih = 1
		self.senang = 2
		self.terkejut = 3
	
	def get_expression(self, exp):
		if exp == self.netral:
			return "netral"
		elif exp == self.sedih:
			return "sedih"
		elif exp == self.senang:
			return "senang"
		elif exp == self.terkejut:
			return "terkejut"
		else:
			return "Tidak dikenal"