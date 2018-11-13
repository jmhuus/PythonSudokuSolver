MAX = 8
MIN = 0

board = [
	[0,5,0,6,0,3,0,0,0],
	[0,8,0,0,0,0,9,4,0],
	[0,0,0,0,0,0,1,0,0],
	[0,0,8,0,0,0,4,7,0],
	[0,7,0,0,2,9,0,0,0],
	[0,0,5,3,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,4],
	[0,3,6,0,0,5,0,0,2],
	[8,0,0,1,9,0,0,0,0]
]



class Solver():

	def __init__(self, board):
		self.board = board




	def toString(self):
		for row in range(MIN, MAX + 1):
			print(board[row])



	def isSolution(self, row, col, potentialSolution):
		if not validateBoard(board):
			return False


			

	def getNextAvailableAddress(self, row, col):
		while(1==1):
			# End of the board?
			if row==MAX and col==MAX:
				print("max found")
				return None

			# End of the row
			if col==MAX:	
				row += 1
				col = MIN
			else:
				col += 1

			# Next available address found, return result
			if board[row][col]==0:
				return {"row":row, "column":col}

	def validateBoard(self):
		# Validate each row
		for row in range(MIN, MAX+1):

			# Remove zeros
			rowArray = list(filter(lambda a: a != 0, board[row]))

			# Ensure unique value
			if len(rowArray) != len(set(rowArray)):
				print("invalid row: {}".format(row))
				return False

		# Validate each column
		for column in range(MIN, MAX+1):

			# Build column array
			for row in range(MIN, MAX+1):
				columnArray = board[row][column]

			# Remove zeros
			columnArray = list(filter(lambda a: a != 0, columnArray))

			# Ensure unique values
			if len(columnArray) != len(set(columnArray)):
				print("invalid column: {}".format(column))
				return False

		# Validate each grid
		for grid in range(MIN+1, MAX+2):
			gridArray = self.getGridArray(grid)

			# Remove zeros
			gridArray = list(filter(lambda a: a != 0, gridArray))

			print("invalid column: {}".format(column))
			if len(gridArray) != len(set(gridArray)):
				return False




		return True

	def solve(self):
		print(self.validateBoard())
		# startingRow = 0
		# startingCol = 0
		# if board[startingRow][startingCol] != 0:
		# 	getNextAvailableAddress['row']
		# 	startingRow = getNextAvailableAddress['row']
		# 	startingCol = getNextAvailableAddress['column']

		# 	for i in range(1, MAX+1):
		# 		if isSolution():

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
					gridArray.append(board[row][col])


		return gridArray








solver = Solver(board)
solver.solve()