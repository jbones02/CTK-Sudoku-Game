import customtkinter as ctk
import hexColors as hex
import boardSubFrame

class Board:
    def __createSubGrids(self):
        numRows = 3
        numCols = 3
        self.__boardSubFrames = []
        for row in range(numRows):
            for col in range(numCols):
                curSubFrame = boardSubFrame.BoardSubFrame(self.__boardFrame, row, col)
                self.__boardSubFrames.append(curSubFrame)
                self.__boardFrame.grid_columnconfigure(col, weight=1)
            self.__boardFrame.grid_rowconfigure(row, weight=1)

    def __setupBoard

    def __init__(self, masterFrame):
        self.__boardFrame = ctk.CTkFrame(master=masterFrame, fg_color=hex.LIGHT_GREY)
        self.__boardFrame.place(relx=0.5, rely=0.475, relwidth=0.9, relheight=0.75, anchor='center')
        self.__setupBoard
        self.__createSubGrids()
