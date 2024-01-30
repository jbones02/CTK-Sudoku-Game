import customtkinter as ctk
import menuScreen

class Game:
    
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

    def __toMenuScreen(self):
        menuScrn = menuScreen.MenuScreen(self.__window)
        menuScrn.display()

    def __toPlayScreen(self):
        playScrn = playScreen.PlayScreen(self.__window)
        playScrn.display()

    def play(self):
        self.__window = ctk.CTk()
        self.__window.title('Sudoku')
        self.__window.geometry('350x500')
        self.__toMenuScreen()
        self.__window.mainloop()