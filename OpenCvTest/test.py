
import numpy as np
import cv2 as cv
from pprint import pprint




class Board():

	MAX_VALUE = 255
	kernel = np.ones((3,3),np.uint8)
	rawImage = None


	# Load image array - [row][column][RGB]
	def __init__(self, filePath):
		self.rawImage = cv.imread(filePath)


	# Returns 2D array of sudoku board
	def grabSudokuBoard(self):
		preProcessedImage = self.getPreProcessedImage(self.rawImage)
		cells = self.getCellContours(preProcessedImage)
	

	# Simple preprocessing
	def getPreProcessedImage(self, img):
		img = cv.GaussianBlur(img, (3,3), 0)
		ret, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

		return img


	# Return an array of cell coordinates
	def getCellContours(self, preProcessedImage):
		img_eroded = cv.erode(preProcessedImage, self.kernel, iterations=1)
		edges = cv.Canny(img_eroded,100,200)
		edges, contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

		cells = []					# Final contours to use as ROI(Region Of Interest)
		alreadyVisitedContours = []	# List of visisted coordinates; some contours have the exact same location
		for i in range(len(contours)):

			# Curent contour (selection area)
			cnt = contours[i]

			# Find all cell-like contours (cells that store sudoku numbers)
			alreadyVisited = cnt[0][0].tolist() in alreadyVisitedContours
			areaGreaterThan = cv.contourArea(cnt) >= 700
			areaSmallerThan = cv.contourArea(cnt) <= 1200
			if areaGreaterThan and areaSmallerThan and not alreadyVisited:
				alreadyVisitedContours.append(cnt[0][0].tolist())
				cells.append(cnt)

		return cells
		
		




filePath = "../test_images/expert_02.PNG"
imageProcessing = Board(filePath)
imageProcessing.grabSudokuBoard()
