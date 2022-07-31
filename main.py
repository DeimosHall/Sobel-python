from filters import border_filter
from filters import OpenCV

path = "sources/t3.tiff"
image_1 = OpenCV.Filter(path)
image_1.show_size()
image_1.show_image()
# image_1.show_gray_image()
# image_1.show_borders()
image_1.show_threshold()
pixel = image_1.get_top_left_border()
# 49, 132 - 308, 171
print(pixel)
image_1.cut_image()