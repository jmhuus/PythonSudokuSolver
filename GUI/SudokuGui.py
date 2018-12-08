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

        bgImage = tk.PhotoImage(file="blank-sudoku-grid.png")
        bgLabel = tk.Label(self, image=bgImage)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        # Init frames
        self.boardFrame = tk.Frame(self)
        self.buttonFrame = tk.Frame(self)

        # Init widgets
        self.cells = {}
        for row in range(9):
        	for col in range(9):
        		self.cells[str(row)+str(col)] = tk.Entry(self.boardFrame, width=4)


        self.cancel = tk.Button(self.buttonFrame, text="Cancel", command=self.quit)
        self.solveBoard = tk.Button(self.buttonFrame, text="Solve", command=self.solveBoard)


        # Place frames
        self.boardFrame.pack(side="top", padx=30, pady=10)
        self.buttonFrame.pack(side="bottom", padx=10, pady=10)


        # Pack the widgets
        self.solveBoard.grid(column=0, row=1)
        self.cancel.grid(column=1, row=1)
        for row in range(9):
        	for col in range(9):
        		address = str(row)+str(col)
        		self.cells[address].grid(row=row, column=col)
        
        

    def solveBoard(self):
    	# Retrieve user input

    	# Solve board

    	# Display result
    	print("solved")


app = SampleApp()
app.mainloop()
