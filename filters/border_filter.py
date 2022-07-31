import numpy as np
import cv2


class ManualSobel:

    def __init__(self, img):
        self._img = img
        self._img_rows = np.size(img, 0)
        self._img_cols = np.size(img, 1)
        self._img_borders = np.zeros(self._img.shape)
        self.width_img = img.shape[0]
        self.height_img = img.shape[1]
        self._gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        self._gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        self._kernel_rows_index = 0
        self._kernel_cols_index = 0
        self._img_rows_index = 0
        self._img_cols_index = 0
        self._a = 0
        self._num = 0

    def get_borders(self):
        while self._img_rows_index < self._img_rows - 2:
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
                self._img_borders[self._img_rows_index + 1, self._img_cols_index + 1] = self._num
                self._img_cols_index += 1
                self._num = 0
            self._img_cols_index = 0  # This resets the x-axis for a new convolution in a new row
            self._img_rows_index += 1
            self._num = 0

        return self._img_borders

    def show_img(self):
        cv2.imshow("image", self._img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_size(self):
        print("Image size")
        print(f"Width: {self.width_img}, Height: {self.height_img}")
