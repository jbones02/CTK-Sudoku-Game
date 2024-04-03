import customtkinter as ctk
import hexColors as hex

class BoardSubFrame():
    def __createTiles(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                button = ctk.CTkButton(self.__boardSubFrame, command=print('press'))
                button.grid(row=row, column=col, sticky='nsew')
                self.__boardSubFrame.grid_columnconfigure(col, weight=1)
            self.__boardSubFrame.grid_rowconfigure(row, weight=1)
            
    
    def __init__(self, master, row, col):
        self.numRows = 3
        self.numCols = 3
        self.__rowInBoard = row
        self.__colInBorad = col
        self.__boardSubFrame = ctk.CTkFrame(master=master, fg_color=hex.BLACK)
        self.__boardSubFrame.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        self.__createTiles()