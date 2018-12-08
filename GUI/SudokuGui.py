# import tkinter as tk
    

# def solveBoard():
#     print("Tkinter is easy to use!")

# def retrieve_input():
# 	input = cell00input.get()
# 	print(input)


# cell00input = ""


# root = tk.Tk()


# # Root size to 500h 500w
# root.geometry("500x500")
# back = tk.Frame(master=root, bg='black')

# # Frame to encompass widgets
# frame = tk.Frame(root)
# frame.pack(padx=10, pady=5)

# # Sudoku cell text boxes
# cell00 = tk.Entry(frame, width=2, height=1, textvariable=cell00input)
# cell00.grid(column=0, row=1)

# # Buttons
# btnSolve = tk.Button(frame, text="Solve", fg="red", command=solveBoard)
# btnSolve.grid(column=0, row=2)
# btnCancel = tk.Button(frame, text="Cancel", command=quit)
# btnCancel.grid(column=1, row=2)


# root.mainloop()






import tkinter as tk

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
        

    def solveBoard(self):
    	# Retrieve user input

    	# Solve board

    	# Display result
    	print("solved")


app = SampleApp()
app.mainloop()
