
import numpy as np
import cv2 as cv
from pprint import pprint


MAX_VALUE = 255


class ProcessImage():


	def __init__(self, filePath):
		# Loads 3D array of the image into RGB; [row][column][RGB]
		self.img = cv.imread(filePath)
		self.imageBase = filePath.split("/")
		self.imageBase = self.imageBase[len(self.imageBase)-1]   
		self.imageBase = self.imageBase.split(".")[0]


	def proccessImage(self):
		self.preProcessing()
		self.findOuterBoarder()
		self.saveImage()


	def preProcessing(self):
		# Gaussian Blur
		kernelSize = 3
		# self.img = cv.GaussianBlur(src=self.img, ksize=(kernelSize,kernelSize), sigmaX=0)

		# Thresholding
		ret, self.img = cv.threshold(src=self.img, thresh=127, maxval=MAX_VALUE, type=cv.THRESH_BINARY)


	def findOuterBoarder(self):
		# Object to be found=white; background=black
		im2, contours, hierarchy = cv2.findContours(image=self.img, contours=cv.RETR_TREE, hierarchy=cv.CHAIN_APPROX_SIMPLE)
	

	def saveImage(self):
		extension = "png"
		cv.imwrite(self.imageBase + "." + extension, self.img)




filePath = "../test_images/expert_02.PNG"
imageProcessing = ProcessImage(filePath)
imageProcessing.proccessImage()
