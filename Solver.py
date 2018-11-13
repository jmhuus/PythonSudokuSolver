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

	def solve(self):
		# startingRow = 0
		# startingCol = 0
		# if board[startingRow][startingCol] != 0:
		# 	getNextAvailableAddress['row']
		# 	startingRow = getNextAvailableAddress['row']
		# 	startingCol = getNextAvailableAddress['column']

		# 	for i in range(1, MAX+1):
		# 		if isSolution():



solver = Solver(board)
solver.solve()