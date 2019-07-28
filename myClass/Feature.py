import math

class Feature:
    def __init__(self):
        #netral
        self.dist_eye_lip_r = 0
        self.dist_eye_lip_l = 0
        self.dist_nose_lip_t = 0
        self.dist_nose_lip_b = 0
        self.dist_lip_r_l = 0
        self.dist_lip_t_b = 0
        # expression
        self.dist_corner_lip_r = None
        self.dist_corner_lip_l = None
        self.dist_lip_t = None
        self.dist_lip_b = None
        self.dist_nose = None
        self.dist_eye_r = None
        self.dist_eye_l = None

    def get_feature_netral(self):
        return {
            "dist_eye_lip_r" : self.dist_eye_lip_r,
            "dist_eye_lip_l" : self.dist_eye_lip_l,
            "dist_nose_lip_t" : self.dist_nose_lip_t,
            "dist_nose_lip_b" : self.dist_nose_lip_b,
            "dist_lip_r_l" : self.dist_lip_r_l,
            "dist_lip_t_b" : self.dist_lip_t_b
        }
    
    def get_feature_expression(self):
        return {
            "dist_corner_lip_r" : self.dist_corner_lip_r,
            "dist_corner_lip_l" : self.dist_corner_lip_l,
            "dist_lip_t" : self.dist_lip_t,
            "dist_lip_b" : self.dist_lip_b,
            "dist_nose" : self.dist_nose,
            "dist_eye_r" : self.dist_eye_r,
            "dist_eye_l" : self.dist_eye_l
        }
    
    def calculation_netral(self, landmarks):
        self.dist_eye_lip_r = self._distance(landmarks[0], landmarks[3])
        self.dist_eye_lip_l = self._distance(landmarks[1], landmarks[4])
        self.dist_nose_lip_t = self._distance(landmarks[2], landmarks[5])
        self.dist_nose_lip_b = self._distance(landmarks[2], landmarks[6])
        self.dist_lip_r_l = self._distance(landmarks[3], landmarks[4])
        self.dist_lip_t_b = self._distance(landmarks[5], landmarks[6])

    def calculation_expression(self, lmk_ntrl, lmk_peak):
        self.dist_eye_r = self._distance(lmk_ntrl[0], lmk_peak[0])
        self.dist_eye_l = self._distance(lmk_ntrl[1], lmk_peak[1])
        self.dist_nose = self._distance(lmk_ntrl[2], lmk_peak[2])
        self.dist_corner_lip_r = self._distance(lmk_ntrl[3], lmk_peak[3])
        self.dist_corner_lip_l = self._distance(lmk_ntrl[4], lmk_peak[4])
        self.dist_lip_t = self._distance(lmk_ntrl[5], lmk_peak[5])
        self.dist_lip_b = self._distance(lmk_ntrl[6], lmk_peak[6])

    def _distance(self, A, B):
        X = A.x - B.x
        Y = A.y - B.y
        return math.sqrt((X ** 2) + (Y ** 2))