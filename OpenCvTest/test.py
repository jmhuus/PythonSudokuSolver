
import numpy as np
import cv2 as cv
from pprint import pprint


MAX_VALUE = 255
kernel = np.ones((3,3),np.uint8)


# Preprocessing
img = cv.imread("../test_images/puzzle_01.jpg")
img = cv.GaussianBlur(img, (3,3), 0)
ret, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
img_eroded = cv.erode(img,kernel,iterations=1)
cv.imwrite("after_eroded.png", img_eroded)

# Retreive and draw contours
edges = cv.Canny(img_eroded,100,200)
edges, contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

visitedContours = []	# Coordinates already visited
cells = []				# list of nparray
for i in range(len(contours)):
	cnt = contours[i]
	alreadyInVisisted = cnt[0][0].tolist() in visitedContours
	areaGreaterThan = cv.contourArea(cnt) >= 700
	areaSmallerThan = cv.contourArea(cnt) <= 1200
	print("i={}   area:{}".format(i, cv.contourArea(cnt)))
	if areaGreaterThan and areaSmallerThan and not alreadyInVisisted:
		visitedContours.append(cnt[0][0].tolist())
		cells.append(cnt)

cv.drawContours(img, cells, -1, (0,255,0), 3)
cv.imwrite("final.png", img)



# class ProcessImage():


# 	def __init__(self, filePath):
# 		# Loads 3D array of the image into RGB; [row][column][RGB]
# 		self.img = cv.imread(filePath)
# 		self.imageBase = filePath.split("/")
# 		self.imageBase = self.imageBase[len(self.imageBase)-1]   
# 		self.imageBase = self.imageBase.split(".")[0]


# 	def proccessImage(self):
# 		self.preProcessing()
# 		self.findOuterBoarder()
# 		self.saveImage()


# 	def preProcessing(self):
# 		# Gaussian Blur
# 		kernelSize = 3
# 		# self.img = cv.GaussianBlur(src=self.img, ksize=(kernelSize,kernelSize), sigmaX=0)

# 		# Thresholding
# 		ret, self.img = cv.threshold(src=self.img, thresh=127, maxval=MAX_VALUE, type=cv.THRESH_BINARY)


# 	def findOuterBoarder(self):
# 		# Object to be found=white; background=black
# 		im2, contours, hierarchy = cv.findContours(self.img.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
	

# 	def saveImage(self):
# 		extension = "png"
# 		cv.imwrite(filename=self.imageBase + "." + extension, image=self.img)




# filePath = "../test_images/expert_02.PNG"
# imageProcessing = ProcessImage(filePath)
# imageProcessing.proccessImage()
