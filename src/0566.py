import numpy as np

class Solution(object):
    def matrixReshape(self, mat, r, c):
        try:
            return np.reshape(mat, (r, c)).tolist()
        except:
            return mat