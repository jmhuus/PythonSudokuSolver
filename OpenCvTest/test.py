
import numpy as np
import cv2 as cv
from pprint import pprint




class Board():

	MAX_VALUE = 255
	guassianBlurKernel = (5,5)
	dialateKernel = np.ones((7,7),np.uint8)
	erodeKernel = np.ones((3,3),np.uint8)
	rawImage = None


	# Load image array - [row][column][RGB]
	def __init__(self, filePath):
		self.filePath = filePath


	# Returns 2D array of sudoku board
	def grabSudokuBoard(self):

		imageProccessOrders = [
								{	"Color":None, "GaussianBlur":(5,5), 	
									"Threshold":[127,255],
									"Canny":[100,200], 					
									"Dialate":np.ones((3,3), np.uint8)	},

								{	"Color":None,
									"Threshold":[127,255],
									"Canny":[100,200],
									"Dialate":np.ones((3,3), np.uint8)	},

								{	"Color":None,
									"Threshold":[127,255],
									"Erode":np.ones((3,3),np.uint8),
									"Canny":[100,200],
									"Dialate":np.ones((3,3), np.uint8)	},

								{	"Color":None,
									"Threshold":[127,255],
									"Erode":np.ones((3,3),np.uint8),
									"GaussianBlur":(5,5),
									"Canny":[100,200],
									"Dialate":np.ones((3,3), np.uint8)	},

								{	"Color":None,
									"GaussianBlur":(3,3),
									"Threshold":[127,255],
									"Erode":np.ones((3,3),np.uint8),
									"Canny":[75,200],
									"Dialate":np.ones((3,3), np.uint8)	},

									# Thin boardered boards
								{	"Color":None,
									"Canny":[100,200],
									"Dialate":np.ones((7,7), np.uint8),
									"GaussianBlur":(5,5),
									"Threshold":[127,255]				},

									# Thin line boards 2
								{	"Color":None,
									"Canny":[30,45],
									"Dialate":np.ones((3,3), np.uint8),
									"Threshold":[127,255],
									"Erode":np.ones((3,3),np.uint8),
									"GaussianBlur":(3,3),
									"Opening":np.ones((2,2), np.uint8)		},

									# Low resolution images
								{	"Color":None,
									"Opening":np.ones((4,4), np.uint8),
									"Canny":[180,250],
									"Opening":np.ones((4,4), np.uint8),
									"GaussianBlur":(3,3),
									"Threshold":[80, 255],
									"Dialate":np.ones((4,4), np.uint8),
									"Erode":np.ones((4,4),np.uint8)		}
							]


		# Retrieve sudoku cell regions
		boardCells = None
		for i in range(len(imageProccessOrders)):

			# Read image
			raw = cv.imread(self.filePath)

			# Process Image
			processedImage = self.getProcessedImage(raw, imageProccessOrders[i])

			# Cell Contours
			cells = self.getCellContours(processedImage)


			height = len(raw)
			width = len(raw[0])


			# 81 distinct cells found
			if len(cells) == 81:
				boardCells = cells
				break

		i = 0
		for cell in cells:
			# Bounding rectangle coordinates
			x, y, w, h = cv.boundingRect(cell)

			# Retrieve min/max values for X/Y
			xMin = x-w
			xMax = x
			yMin = y-h
			yMax = y

			# Build sub-image using the bounding rectangle
			subImage = []
			for row in range(yMin, yMin+1):
				newRow = []
				for col in range(xMin, xMax+1):
					newRow.append(raw[row][col])
				subImage.append(newRow)

			# Save image
			i += 1
			cv.imwrite("cell_{}.png".format(i), np.asarray(subImage))




		
			# 	# Run OCR on ROI temp image

			# 	# Store ROI result into board array
			# 	board = readBoard(cells)
			
			# print("{} {} cells found.".format(i, len(cells)))
			# cv.imwrite("processedImage{}.png".format(i), processedImage)		

			# final = cv.drawContours(raw, cells, -1, (0,255,0), 3)					
			# cv.imwrite("processedImage_withContours{}.png".format(i), final)
			# continue



	

	# Simple preprocessing
	def getProcessedImage(self, img, processOrder):

		for key, value in processOrder.items():
			if key == "GaussianBlur":
				img = cv.GaussianBlur(img, value, 0)
				# cv.imwrite("GaussianBlur.png", img)

			if key == "Threshold":
				ret, img = cv.threshold(img, value[0], value[1], cv.THRESH_BINARY)
				# cv.imwrite("Threshold.png", img)

			if key == "Color":
				img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
				# cv.imwrite("Color.png", img)

			if key == "Canny":
				img = cv.Canny(img.copy(),value[0],value[1])
				# cv.imwrite("Canny.png", img)

			if key == "Dialate":
				img = cv.dilate(img, value, iterations = 1)
				# cv.imwrite("Dialate.png", img)

			if key == "Erode":
				img = cv.erode(img, value, iterations=1)
				# cv.imwrite("Erode.png", img)

			if key == "Opening":
				img = cv.morphologyEx(img, cv.MORPH_OPEN, value)
				# cv.imwrite("Opening.png", img)

		return img


	# Return an array of cell coordinates
	def getCellContours(self, processedImage):

		edges, contours, hierarchy = cv.findContours(processedImage, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

		# Estimate sudoku cell size
		width, height = edges.shape[:2]
		imageArea = width * height
		cellAreaMax = (imageArea * .80) / 81
		cellAreaMin = (imageArea * .50) / 81

		cells = []					# Final contours to use as ROI(Region Of Interest)
		alreadyVisitedContours = []	# List of visited coordinates; some contours have the exact same location
		for i in range(len(contours)):

			# Curent contour (selection area)
			cnt = contours[i]

			# Find all cell-like contours (cells that store Sudoku numbers)
			alreadyVisited = cnt[0][0].tolist() in alreadyVisitedContours
			areaGreaterThan = cv.contourArea(cnt) >= cellAreaMin
			areaSmallerThan = cv.contourArea(cnt) <= cellAreaMax
			if areaGreaterThan and areaSmallerThan and not alreadyVisited:
				alreadyVisitedContours.append(cnt[0][0].tolist())
				cells.append(cnt)

		return cells
		





filePath = "../test_images/expert_02.png"
imageProcessing = Board(filePath)
imageProcessing.grabSudokuBoard()
