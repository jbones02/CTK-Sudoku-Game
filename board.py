import customtkinter as ctk
import requests
import hexColors as hex
import puzzleSubGrid
import puzzle

class Board:
    def __createSubGrids(self):
        numRows = 3
        numCols = 3
        self.__boardSubFrames = []
        for row in range(numRows):
            for col in range(numCols):
                curSubFrame = puzzleSubGrid.PuzzleSubGrid(self.__boardFrame, row, col)
                self.__boardSubFrames.append(curSubFrame)
                self.__boardFrame.grid_columnconfigure(col, weight=1)
            self.__boardFrame.grid_rowconfigure(row, weight=1)

    def __getUnsolvedSubGrids(self):
        self.__unsolvedSubGrids()

    def __generateBoard(self):
        # Use Dosuku API to get puzzle
        response = requests.get('https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}')
        responsePuzzleUnsolved = (response.json().get('newboard').get('grids'))[0].get('value')  # Extract puzzle from response
        responsePuzzleNotes = (response.json().get('newboard').get('grids'))[0].get('value')
        responsePuzzleSolved = (response.json().get('newboard').get('grids'))[0].get('value')

        self.__unsolvedPuzzle = puzzle.Puzzle(responsePuzzleUnsolved)  # Initialize unsolved puzzle
        self.__notesPuzzle = puzzle.Puzzle(responsePuzzleNotes)  # Create copy of unsolved puzzle for notes

        # Initialize solved puzzle
        self.__solvedPuzzle = puzzle.Puzzle(responsePuzzleSolved)

        # Convert zeros in puzzles to None
        self.__unsolvedPuzzle.zerosToNone()
        self.__solvedPuzzle.zerosToNone()

        # Solve generate solution
        self.__solvedPuzzle.solve()

        # Print puzzles to terminal
        self.__unsolvedPuzzle.print()
        self.__solvedPuzzle.print()  
        


    def __setupBoard(self):
        self.__generateBoard()
        self.__createSubGrids()

    def __init__(self, masterFrame):
        self.__boardFrame = ctk.CTkFrame(master=masterFrame, fg_color=hex.LIGHT_GREY)
        self.__boardFrame.place(relx=0.5, rely=0.475, relwidth=0.9, relheight=0.75, anchor='center')
        self.__setupBoard()
