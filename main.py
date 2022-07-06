import numpy as np
from filters import border_filter

img = np.array([[3, 0, 1, 2, 7, 4],
                [1, 5, 8, 9, 3, 1],
                [2, 7, 2, 5, 1, 3],
                [0, 1, 3, 1, 7, 8],
                [4, 2, 1, 6, 2, 8],
                [2, 4, 5, 2, 3, 9]])

sobel1 = border_filter.ManualSobel(img)
sobel1.get_border()
print(sobel1.get_border())
