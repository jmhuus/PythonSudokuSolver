from pprint import pprint
import cv2 as cv
import numpy as np


image = []
for row in range(264, 295):
	newRow = []
	for col in range(263, 297):
		newRow.append([row, col])
	image.append(newRow)

pprint(image)