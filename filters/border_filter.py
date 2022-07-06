import numpy as np


class ManualSobel:

    def __init__(self, img):
        self._img = img
        self._img_rows = np.size(img, 0)
        self._img_cols = np.size(img, 1)
        self._img_copy = np.zeros(self._img.shape)
        self._gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        self._gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        self._kernel_rows_index = 0
        self._kernel_cols_index = 0
        self._img_rows_index = 0
        self._img_cols_index = 0
        self._a = 0
        self._num = 0

    def get_border(self):
        while self._img_cols_index < self._img_cols - 2:
            for i in range(self._img_rows_index, self._img_rows_index + 3):
                for j in range(self._img_cols_index, self._img_cols_index + 3):
                    self._a = self._gx[self._kernel_rows_index, self._kernel_cols_index] * self._img[i, j]
                    self._num += self._a
                    self._kernel_cols_index += 1
                self._kernel_cols_index = 0
                self._kernel_rows_index += 1
            self._kernel_cols_index = 0
            self._kernel_rows_index = 0
            self._img_copy[self._img_rows_index + 1, self._img_cols_index + 1] = self._num
            self._img_cols_index += 1
            self._num = 0

        return self._img_copy
