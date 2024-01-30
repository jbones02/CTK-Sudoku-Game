import customtkinter as ctk
import menuScreen

class Game:
    
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

    def play(self):
        root = ctk.CTk()
        root.title('Sudoku')
        root.geometry('350x500')

        menu = menuScreen.MenuScreen(root)
        root.mainloop()