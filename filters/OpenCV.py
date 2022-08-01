# To see more about sobel filter, go to the documentation
# https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html

import cv2 as cv
import numpy as np


class Filter:

    def __init__(self, path):
        # Image properties
        self._path = path
        self._img = cv.imread(self._path, cv.COLOR_BGR2RGB)
        self._img_width = self._img.shape[1]
        self._img_height = self._img.shape[0]
        self._top_left_edge = [0, 0]
        self._bottom_right_edge = [0, 0]
        self._gray_img = cv.cvtColor(self._img, cv.COLOR_BGR2GRAY)
        # Sobel parameters
        self._scale = 1
        self._delta = 0
        self._ddepth = cv.CV_16S
        # Sobel gradients
        self._grad_x = cv.Sobel(self._gray_img, self._ddepth, 1, 0, ksize=3, scale=self._scale, delta=self._delta,
                                borderType=cv.BORDER_DEFAULT)
        self._grad_y = cv.Sobel(self._gray_img, self._ddepth, 0, 1, ksize=3, scale=self._scale, delta=self._delta,
                                borderType=cv.BORDER_DEFAULT)
        self._abs_grad_x = cv.convertScaleAbs(self._grad_x)
        self._abs_grad_y = cv.convertScaleAbs(self._grad_y)
        # _grad is the average of _abs_grad_x and _abs_grad_y, contains the sobel image
        self._grad = cv.addWeighted(self._abs_grad_x, 0.5, self._abs_grad_y, 0.5, 0)
        # Threshold
        self._thresh = cv.threshold(self._grad, 40, 255, cv.THRESH_BINARY_INV)[1]
        self._contours = cv.findContours(self._thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        self._canvas = np.zeros_like(self._img)

    def show_size(self):
        print("Image size")
        print(f"Width: {self._img_width}, Height: {self._img_height}")

    def show_image(self):
        cv.imshow("Original image", self._img)
        cv.waitKey(0)

    def show_gray_image(self):
        cv.imshow("Gray image", self._gray_img)
        cv.waitKey(0)

    def show_threshold(self):
        cv.imshow("Threshold image", self._thresh)
        cv.waitKey(0)

    def show_borders(self):
        cv.imshow("Grad", self._grad)
        cv.waitKey(0)

    def show_canvas(self):
        cv.imshow("Canvas", self._canvas)
        cv.waitKey(0)

    def calculate_borders(self):
        self._top_left_edge = [self._img_width, self._img_height]
        self._bottom_right_edge = [0, 0]
        counter = 0
        x_limit = 20
        for y in range(0, self._img_height):
            for x in range(0, self._img_width):
                if self._thresh[y, x] == 0:  # Means found a black pixel
                    if counter == x_limit:
                        # print(f"Black found at {x-x_limit},{y} counter = {counter}")
                        # Calculate top_left_edge
                        if y < self._top_left_edge[1]:
                            self._top_left_edge[1] = y
                        if x - x_limit < self._top_left_edge[0]:
                            self._top_left_edge[0] = x - x_limit
                        # print(f"edge: {top_left_edge[0]},{top_left_edge[1]}")
                        # Calculate bottom_right_edge
                        if y > self._bottom_right_edge[1]:
                            self._bottom_right_edge[1] = y
                        if x > self._bottom_right_edge[0]:
                            self._bottom_right_edge[0] = x
                    counter += 1
                else:
                    counter = 0
            x = 0
        print(f"Top edge: {self._top_left_edge[0]},{self._top_left_edge[1]}")
        print(f"Bottom edge: {self._bottom_right_edge[0]},{self._bottom_right_edge[1]}")

    def show_cropped_image(self):
        self.calculate_borders()
        x1 = self._top_left_edge[0]
        y1 = self._top_left_edge[1]
        x2 = self._bottom_right_edge[0]
        y2 = self._bottom_right_edge[1]
        crop = self._img[y1:y2, x1:x2]
        cv.imshow('Image', crop)
        cv.waitKey(0)