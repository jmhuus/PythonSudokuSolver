
import numpy as np
import cv2 as cv
from pprint import pprint




class Board():

	MAX_VALUE = 255
	guassianBlurKernel = (3,3)
	dialateKernel = np.ones((3,3),np.uint8)
	erodeKernel = np.ones((3,3),np.uint8)
	rawImage = None


	# Load image array - [row][column][RGB]
	def __init__(self, filePath):
		self.filePath = filePath


	# Returns 2D array of sudoku board
	def grabSudokuBoard(self):

		imageProccessOrders = [["Color", "GaussianBlur", "Threshold", "Erode", "Canny", "Dialate"],
								["Color", "GaussianBlur", "Threshold", "Erode", "Canny", "Dialate"],
								["Color", "Threshold", "Erode", "GaussianBlur", "Canny", "Dialate"],
								["Color", "Threshold", "Canny", "Dialate"]]


		# Retrieve sudoku cell regions
		for i in range(len(imageProccessOrders)):
			
			# Read image
			raw = cv.imread(self.filePath)

			# Process Image
			processedImage = self.getProcessedImage(raw, imageProccessOrders[i])

			# Cell Contours
			cells = self.getCellContours(processedImage)	

			# Image not well processed
			if len(cells) != 81:
				print("{} cells found.".format(len(cells)))
				cv.imwrite("processedImage{}.png".format(i), processedImage)		

				final = cv.drawContours(raw, cells, -1, (0,255,0), 3)					
				cv.imwrite("processedImage_withContours{}.png".format(i), final)		
				continue


		# Build ROI
		
		# Run OCR on ROI temp image

		# Store ROI result into board array
	

	# Simple preprocessing
	def getProcessedImage(self, img, processOrder):

		print(processOrder)

		for imageProcess in processOrder:
			if imageProcess == "GaussianBlur":
				img = cv.GaussianBlur(img, self.guassianBlurKernel, 0)

			if imageProcess == "Threshold":
				ret, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

			if imageProcess == "Color":
				img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

			if imageProcess == "Canny":
				img = cv.Canny(img,100,200)

			if imageProcess == "Dialate":
				img = cv.dilate(img, self.dialateKernel, iterations = 1)

			if imageProcess == "Erode":
				img = cv.erode(img, self.erodeKernel, iterations=1)

		return img


	# Return an array of cell coordinates
	def getCellContours(self, processedImage):

		edges, contours, hierarchy = cv.findContours(processedImage, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


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
		





filePath = "../test_images/expert_02.png"
imageProcessing = Board(filePath)
imageProcessing.grabSudokuBoard()
