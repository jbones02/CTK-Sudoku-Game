import customtkinter as ctk
import requests
import hexColors as hex
import boardSubFrame
import puzzle

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

    def __generateBoard(self):
        # Use Dosuku API to get puzzle
        response = requests.get('https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}')
        response_puzzle_unsolved = (response.json().get('newboard').get('grids'))[0].get('value')  # Extract puzzle from response
        response_puzzle_notes = (response.json().get('newboard').get('grids'))[0].get('value')
        response_puzzle_solved = (response.json().get('newboard').get('grids'))[0].get('value')

        self.__unsolved_puzzle = puzzle.Puzzle(response_puzzle_unsolved)  # Initialize unsolved puzzle
        self.__notes_puzzle = puzzle.Puzzle(response_puzzle_notes)  # Create copy of unsolved puzzle for notes

        # Generate solution with backtracking method
        self.__solved_puzzle = puzzle.Puzzle(response_puzzle_solved)

        # Convert zeros in puzzles to None
        self.__unsolved_puzzle.zeros_to_none()
        self.__solved_puzzle.zeros_to_none()

        self.__solved_puzzle.solve()

        # Print puzzles to terminal
        self.__unsolved_puzzle.print()
        self.__solved_puzzle.print()  
        


    def __setupBoard(self):
        self.__generateBoard()
        self.__createSubGrids()

    def __init__(self, masterFrame):
        self.__boardFrame = ctk.CTkFrame(master=masterFrame, fg_color=hex.LIGHT_GREY)
        self.__boardFrame.place(relx=0.5, rely=0.475, relwidth=0.9, relheight=0.75, anchor='center')
        self.__setupBoard()
