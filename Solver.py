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
		for row in range(0, MAX + 1):
			print(board[row])

	def solve(self):
		startingRow = 0
		startingCol = 0
		if board[startingRow][startingCol] != 0:

			

	def getNextAvailableAddress(self, row, col):
		if col == MAX:
			

			

			





solver = Solver(board)
solver.solve()