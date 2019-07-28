from imutils import face_utils
from myClass.Point import Point
import dlib
import cv2

class Landmark:
	_p = "assets/shape_predictor_68_face_landmarks.dat"

	def __init__(self, image):
		self._points = [0] * 7
		self._image = image
		self._proses()

	def get_landmark(self):
		return self._points

	def _proses(self):
		image = cv2.imread(self._image)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		h, w, c = image.shape

		detector = dlib.get_frontal_face_detector()
		predictor = dlib.shape_predictor(self._p)
		rects = detector(gray, 0)
		
		shape = predictor(gray, rects[0])
		shape = face_utils.shape_to_np(shape)
	
		i = 0
		X1 = X2 = 0
		for (x, y) in shape:
			i += 1
			# i = 40 sudut mata kanan
			if i == 40:
				self._points[0] = Point(x, y)
				# cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
			# i = 43 sudut mata kiri
			elif i == 43:
				self._points[1] = Point(x, y)
				# cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
			# i = 34 tengah bawah hidung
			elif i == 34:
				self._points[2] = Point(x, y)
				# cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
			# i = 49 sudut bibir kanan
			elif i == 49:
				self._points[3] = Point(x, y)
				# cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
			# i = 55 sudut bibir kiri
			elif i == 55:
				self._points[4] = Point(x, y)
				# cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
			# i = 52 bibir atas
			elif i == 52:
				self._points[5] = Point(x, y)
				# cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
			# i = 58 bibir bawah
			elif i == 58:
				self._points[6] = Point(x, y)
				# cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
			elif i == 1:
				X1 = x
			elif i == 17:
				X2 = x
			
		if X1 != 0 and X2 != 0:
			image = image[0:h, X1:X2]
			w_g = image.shape[1]
			new_w = 80
			ratio = new_w / w_g
			new_h = int(h * ratio)
			image = cv2.resize(image,(new_w, new_h))
			for n, lmk in enumerate(self._points):
				self._points[n].x = (self._points[n].x - X1)* ratio
				self._points[n].y *= ratio
				cv2.circle(image, (int(self._points[n].x), int(self._points[n].y)), 2, (0, 255, 0), -1)

		cv2.imwrite('output_landmark.jpeg', image)