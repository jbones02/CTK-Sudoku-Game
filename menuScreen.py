import customtkinter as ctk
import hexColors

class MenuScreen:

    def __createMenuScreen(self):
        self.__menuScreen = ctk.CTkFrame(master=self.__root, fg_color=hexColors.BABY_BLUE)
        self.__menuScreen.place(relwidth=1, relheight=1)

    def __createTitle(self):
        self.__title = ctk.CTkLabel(master=self.__menuScreen, text="SUDOKU", font=('', 60))
        self.__title.pack(pady=(120, 0))

    def __createCredit(self):
        self.__credit = ctk.CTkLabel(master=self.__menuScreen, text="By Jaryd Bones", font=('', 20))
        self.__credit.pack()

    def __createStartButton(self):
        self.__startButton = ctk.CTkButton(master=self.__menuScreen, text="START", command=self.startGame)
        self.__startButton.pack(pady=(20, 0))

    def __createQuitButton(self):
        self.__quitButton = ctk.CTkButton(master=self.__menuScreen, text="QUIT", command=self.quitGame)
        self.__quitButton.pack(pady=(5, 0))

    def __init__(self, root):
        self.__root = root
        self.__createMenuScreen()
        self.__createTitle()
        self.__createCredit()
        self.__createStartButton()
        self.__createQuitButton()

    def startGame(self):
        print("Game started")

    def quitGame(self):
        print("Game ended")
        self.__root.destroy()
