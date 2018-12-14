from pprint import pprint

MAX = 8
MIN = 0



class Solver():

	def __init__(self, board):
		self.board = board


	def solve(self):
		# Locate the first unsolved cell
		startingRow = 0
		startingCol = 0
		if self.board[startingRow][startingCol] != 0:
			startingRow = self.getNextAvailableAddress(startingRow, startingCol)['row']
			startingCol = self.getNextAvailableAddress(startingRow, startingCol)['column']

		# Use the first unsolved cell to begin recursion isSolution()
		for i in range(1, MAX+1):
			if self.isSolution(startingRow, startingCol, i):
				return self.board


		return self.board


	def isSolution(self, row, col, potentialSolution):
		# New solution placement
		self.board[row][col] = potentialSolution

		# Invalid placement
		if not self.validateBoard():
			self.board[row][col] = 0
			return False

		# Current placement works, try the next; get the next address
		nextAddress = self.getNextAvailableAddress(row, col)
		if nextAddress is None:
			return True
		# print("{} {}".format(nextAddress['row'], nextAddress['column']))

		# Try subsequent solutions
		for nextPotentialSolution in range(MIN+1, MAX+2):  # 1-9
			# print("trying solution {} for row:{} column:{}".format(nextPotentialSolution, row, col))
			if self.isSolution(nextAddress['row'], nextAddress['column'], nextPotentialSolution):
				return True

		# All subsequent solutions were invalid
		self.board[row][col] = 0
		return False


	def getNextAvailableAddress(self, row, col):
		while True:
			# End of the board?
			if row==MAX and col==MAX:
				return None

			# End of the row
			if col==MAX:	
				row += 1
				col = MIN
			else:
				col += 1

			# Next available address found, return result
			if self.board[row][col]==0:
				return {"row":row, "column":col}


	def validateBoard(self):
		# Validate each row
		for row in range(MIN, MAX+1):
			
			# Remove zeros
			rowArray = list(filter(lambda a: a != 0, self.board[row]))

			# Ensure unique value
			if len(rowArray) != len(set(rowArray)):
				# print("invalid row: {}".format(rowArray))
				return False

		# Validate each column
		for column in range(MIN, MAX+1):

			# Build column array
			columnArray = []
			for row in range(MIN, MAX+1):
				columnArray.append(self.board[row][column])

			# Remove zeros
			columnArray = list(filter(lambda a: a != 0, columnArray))

			# Ensure unique values
			if len(columnArray) != len(set(columnArray)):
				# print("invalid column: {}".format(columnArray))
				return False

		# Validate each grid
		for grid in range(MIN+1, MAX+2):
			gridArray = self.getGridArray(grid)

			# Remove zeros
			gridArray = list(filter(lambda a: a != 0, gridArray))

			# Ensure unique values
			if len(gridArray) != len(set(gridArray)):
				# print("invalid grid: {}".format(gridArray))
				return False

		# Everything checks out
		return True


	def getGridArray(self, gridIndex):
		# TODO: refactor to account for varying sudoku puzzle sizes (use MIN/MAX)
		gridDictionary = {
							1:[[0,1,2],[0,1,2]],
							2:[[0,1,2],[3,4,5]],
							3:[[0,1,2],[6,7,8]],
							4:[[3,4,5],[0,1,2]],
							5:[[3,4,5],[3,4,5]],
							6:[[3,4,5],[6,7,8]],
							7:[[6,7,8],[0,1,2]],
							8:[[6,7,8],[3,4,5]],
							9:[[6,7,8],[6,7,8]]}

		gridArray = []

		for row in range(MIN, MAX+1):
			for col in range(MIN, MAX+1):
				if row in gridDictionary[gridIndex][0] and col in gridDictionary[gridIndex][1]:
					gridArray.append(self.board[row][col])


		return gridArray


	def toString(self):
		return self.board