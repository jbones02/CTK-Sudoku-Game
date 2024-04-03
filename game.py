import customtkinter as ctk
import menuScreen
import playScreen

class Game:
    
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

    def toMenuScreen(self):
        menuScrn = menuScreen.MenuScreen(self.__window, self)
        menuScrn.display()

    def toPlayScreen(self):
        playScrn = playScreen.PlayScreen(self.__window)
        playScrn.display()

    def play(self):
        self.__window = ctk.CTk()
        self.__window.title('Sudoku')
        self.__window.geometry('400x500')
        self.__window.resizable(False, False)
        self.toMenuScreen()
        self.__window.mainloop()