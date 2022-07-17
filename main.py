import numpy as np
from filters import border_filter
import cv2

img2 = np.array([[3, 0, 1, 2, 7, 4],
                [1, 5, 8, 9, 3, 1],
                [2, 7, 2, 5, 1, 3],
                [0, 1, 3, 1, 7, 8],
                [4, 2, 1, 6, 2, 8],
                [2, 4, 5, 2, 3, 9]])

path = "2022-07-08_12-42.png"
img = cv2.imread(path)
img = np.asarray(img)
print(img.shape)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)
print(gray_img)

image_1 = border_filter.ManualSobel(img)
image_1.show_img()
sobel_image = image_1.get_borders()
print(sobel_image)
print('Program finished')