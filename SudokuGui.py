import tkinter as tk
from pprint import pprint
import sys
from Solver import Solver



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
        self.cancel = tk.Button(self.buttonFrame, text="Cancel", command=self.quit)
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


    def notifyUser(self, message):
        print(message)


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
        pprint(solvedBoard)

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


app = SampleApp()
app.mainloop()

