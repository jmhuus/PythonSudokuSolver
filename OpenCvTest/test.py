
import numpy as np
import cv2 as cv
from pprint import pprint




class Board():

	MAX_VALUE = 255
	dialateKernel = np.ones((5,5),np.uint8)
	rawImage = None


	# Load image array - [row][column][RGB]
	def __init__(self, filePath):
		self.rawImage = cv.imread(filePath)


	# Returns 2D array of sudoku board
	def grabSudokuBoard(self):
		# Retrieve sudoku cell regions
		preProcessedImage = self.getPreProcessedImage(self.rawImage)
		cells = self.getCellContours(preProcessedImage)

		# Image not well processed
		if len(cells) != 81:
			print("error: trouble finding all sudoku cells. {} cells found.".format(len(cells)))

		final = cv.drawContours(preProcessedImage, cells, -1, (0,255,0), 3)
		cv.imwrite("final.png", final)

		# Build ROI
		

		# Run OCR on ROI temp image

		# Store ROI result into board array
	

	# Simple preprocessing
	def getPreProcessedImage(self, img):
		img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		cv.imwrite("after_cvtColor.jpg", img)
		ret, img = cv.threshold(img, 210, 255, cv.THRESH_BINARY)
		cv.imwrite("after_threshold.jpg", img)
		img = cv.GaussianBlur(img, (3,3), 0)
		cv.imwrite("after_guassian.jpg", img)

		return img


	# Return an array of cell coordinates
	def getCellContours(self, processedImage):
		edges = cv.Canny(processedImage,100,200)
		cv.imwrite("after_canny.jpg", edges)
		edges = cv.dilate(edges, self.dialateKernel, iterations = 1)
		cv.imwrite("after_dialate.jpg", edges)
		edges, contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)




		for i in range(10):
			allContours = cv.drawContours(self.rawImage, contours[i], -1, (0,255,0), 3)
			print("contour: {}   size: {}".format(i, cv.contourArea(contours[i])))
			cv.imwrite("allContours{}.png".format(i), allContours)




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
		





filePath = "../test_images/puzzle_02.jpg"
imageProcessing = Board(filePath)
imageProcessing.grabSudokuBoard()
