from filters import border_filter
from filters import OpenCV

path = "sources/t3.tiff"
image_1 = OpenCV.Filter(path)
image_1.show_size()
image_1.show_image()
# image_1.show_gray_image()
# image_1.show_borders()
pixel = image_1.calculate_borders()
# image_1.show_threshold()
print(pixel)
image_1.show_cropped_image()