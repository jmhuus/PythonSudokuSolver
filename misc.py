from pprint import pprint
import cv2 as cv
import numpy as np


# [[RGB, RGB, RGB, RGB, RGB, RGB], [RGB, RGB, RGB, RGB, RGB, RGB]]
subImage = []
for row in range(x):
	newRow = []
	for col in range(500):
		newRow.append([255,0,0])

	subImage.append(newRow)

cv.imwrite("customImage.png", np.asarray(subImage))