import tkinter as tk
from pprint import pprint
import sys
from pprint import pprint

MAX = 8
MIN = 0



class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Window size
        # self.geometry("500x500")
        self.title("Sudoku Solver")

        # Build widgets
        self.initButtons()
        self.initSudokuBoard()
        self.initMessageDisplay()

    def initButtons(self):
        # Frame
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.pack(side="bottom", padx=10, pady=10)

        # Buttons
        self.cancel = tk.Button(self.buttonFrame, text="Close", command=self.quit)
        self.resetBoard = tk.Button(self.buttonFrame, text="Reset", command=self.resetBoard)
        self.solveBoard = tk.Button(self.buttonFrame, text="Solve", command=self.solveBoard)
        self.solveBoard.grid(column=0, row=1)
        self.resetBoard.grid(column=1, row=1)
        self.cancel.grid(column=2, row=1)

    def initSudokuBoard(self):
        # Frame
        self.boardFrame = tk.Frame(self)
        self.boardFrame.pack(side="top", padx=30, pady=10)

        # Build entries
        self.cells = {}
        for row in range(9):
            for col in range(9):
                self.cells[str(row)+str(col)] = tk.Entry(self.boardFrame, width=4)

        # Place entries into grid
        for row in range(9):
            for col in range(9):
                address = str(row)+str(col)

                # Row padding
                if (row+1)%3 == 0:
                    pady=(0,4)
                else:
                    pady=0

                # Column padding
                if (col+1)%3 == 0:
                    padx=(0,4)
                else:
                    padx=0

                # Place cell into grid
                self.cells[address].grid(row=row, column=col, padx=padx, pady=pady)

    def initMessageDisplay(self):
        # Frame
        self.messageFrame = tk.Frame(self)
        self.messageFrame.pack(side="bottom", padx=10, pady=10)

        # Buttons
        self.messageLabel = tk.Label(self.messageFrame)
        self.messageLabel.grid(column=1, row=2)
     

    def retreiveBoard(self):

        # Build array from user input
        board = []
        for row in range(9):

            # Build one row at a time
            newRow = []
            for col in range(9):

                # Ensure user input is correct during retrieval
                # TODO: ensure integers 1-9
                address = str(row)+str(col)
                try:
                    if self.cells[address].get() != '':
                        newRow.append(int(self.cells[address].get()))
                    else:
                        newRow.append(int(0))
                except ValueError:
                    self.notifyUser("Non-number found in cell.")
                    return None

            # Append row to board
            board.append(newRow)
        return board

    def solveBoard(self):
        
        # Retrieve user input
        board = self.retreiveBoard()
        if board==None:
            return

        # Solve board
        solver = Solver(board)
        solvedBoard = solver.solve()

        # Display result
        for row in range(9):
            for col in range(9):

                address = str(row)+str(col)
                self.cells[address].delete(0, 'end')
                self.cells[address].insert(0, solvedBoard[row][col])

        # Display solved
        self.messageLabel.config(text="Solved!")

    def resetBoard(self):

    	# Empty entire grid
    	for row in range(9):
    		for col in range(9):
    			address = str(row)+str(col)
    			self.cells[address].delete(0, 'end')

    	# Set cursor to (0,0) cell
    	self.cells[str(0)+str(0)].icursor(0)

    	# Empty display message
    	self.messageLabel.config(text="")


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

		# Try subsequent solutions
		for nextPotentialSolution in range(MIN+1, MAX+2):  # 1-9
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
				return False

		# Validate each grid
		for grid in range(MIN+1, MAX+2):
			gridArray = self.getGridArray(grid)

			# Remove zeros
			gridArray = list(filter(lambda a: a != 0, gridArray))

			# Ensure unique values
			if len(gridArray) != len(set(gridArray)):
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



# Open UI
app = SampleApp()
app.mainloop()

