import customtkinter as ctk
import hexColors as hex

class MenuScreen:

    def __createMenuScreenFrame(self):
        self.__menuScreen = ctk.CTkFrame(master=self.__window, fg_color=hex.BABY_BLUE)
        self.__menuScreen.place(relwidth=1, relheight=1)

    def __createTitle(self):
        self.__title = ctk.CTkLabel(master=self.__menuScreen, text="SUDOKU", font=('', 60))
        self.__title.pack(pady=(120, 0))

    def __createCredit(self):
        self.__credit = ctk.CTkLabel(master=self.__menuScreen, text="By Jaryd Bones", font=('', 20))
        self.__credit.pack()

    def __createStartButton(self):
        self.__startButton = ctk.CTkButton(master=self.__menuScreen, text="START", command=self.__startGame)
        self.__startButton.pack(pady=(20, 0))

    def __createQuitButton(self):
        self.__quitButton = ctk.CTkButton(master=self.__menuScreen, text="QUIT", command=self.__quitGame)
        self.__quitButton.pack(pady=(5, 0))

    def __init__(self, window, game):
        self.__window = window
        self.__game = game

    def display(self):
        self.__createMenuScreenFrame()
        self.__createTitle()
        #self.__createCredit()
        self.__createStartButton()
        self.__createQuitButton()

    def __startGame(self):
        print("Game started")
        self.__menuScreen.destroy()
        self.__game.toPlayScreen()

        

    def __quitGame(self):
        print("Game ended")
        self.__window.destroy()
