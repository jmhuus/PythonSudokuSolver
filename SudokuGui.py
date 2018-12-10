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
        


    def initButtons(self):
        # Frame
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.pack(side="bottom", padx=10, pady=10)

        # Buttons
        self.cancel = tk.Button(self.buttonFrame, text="Cancel", command=self.quit)
        self.solveBoard = tk.Button(self.buttonFrame, text="Solve", command=self.solveBoard)
        self.solveBoard.grid(column=0, row=1)
        self.cancel.grid(column=1, row=1)

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
        

    def retreiveBoard(self):
        board = []
        for row in range(9):
            newRow = []
            for col in range(9):
                address = str(row)+str(col)

                try:
                    if self.cells[address].get() != '':
                        newRow.append(int(self.cells[address].get()))
                    else:
                        newRow.append(int(0))
                except ValueError:
                    self.notifyUser("Non-number found in cell.")
                    return None


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
        print("solved")
        pprint(solvedBoard)


app = SampleApp()
app.mainloop()

