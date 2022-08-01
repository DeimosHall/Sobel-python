from filters import border_filter
from filters import OpenCV

path = "sources/t2_1.tiff"
image_1 = OpenCV.Filter(path)
image_1.show_size()
image_1.show_image()
# image_1.show_gray_image()
# image_1.show_borders()
# image_1.show_threshold()
image_1.show_cropped_image()