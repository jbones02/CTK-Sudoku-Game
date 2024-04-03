import customtkinter as ctk
import board
import hexColors

class PlayScreen:
    def __init__(self, window):
        self.__window = window

    def __createPlayScreenFrame(self):
        self.__menuScreenFrame = ctk.CTkFrame(master=self.__window, fg_color=hexColors.BABY_BLUE)
        self.__menuScreenFrame.place(relwidth=1, relheight=1)

    def __createPlayScreenBoard(self):
        self.__gameBoard = board.Board(self.__menuScreenFrame)

    def display(self):
        self.__createPlayScreenFrame()
        self.__createPlayScreenBoard()