class Puzzle:
    def __init__ (self, board):
        self.__board = board

    def __getBoxofNum(self, row, col):
        # Boxes are 0 indexed starting in the top left
                # Get box of num
        if (0 <= row <= 2) and (0 <= col <= 2):  # If in box 0
            return 0
        elif ((0 <= row <= 2) and (3 <= col <= 5)):  # If in box 1
            return 1
        elif ((0 <= row <= 2) and (6 <= col <= 8)):  # If in box 2
            return 2
        elif ((3 <= row <= 5) and (0 <= col <= 2)):  # If in box 3
            return 3
        elif ((3 <= row <= 5) and (3 <= col <= 5)):  # If in box 4
            return 4
        elif ((3 <= row <= 5) and (6 <= col <= 8)):  # If in box 5
            return 5
        elif ((6 <= row <= 8) and (0 <= col <= 2)):  # If in box 6
            return 6
        elif ((6 <= row <= 8) and (3 <= col <= 5)):  # If in box 7
            return 7
        elif ((6 <= row <= 8) and (6 <= col <=8)):
            return 8
        else:
            return None
        
    def __getNumsInBox(self, boxNum):
        if (boxNum == 0):
            return [self.__board[0][0], self.__board[0][1], self.__board[0][2],
                    self.__board[1][0], self.__board[1][1], self.__board[1][2],
                    self.__board[2][0], self.__board[2][1], self.__board[2][2]]
        elif (boxNum == 1):
            return [self.__board[0][3], self.__board[0][4], self.__board[0][5],
                    self.__board[1][3], self.__board[1][4], self.__board[1][5],
                    self.__board[2][3], self.__board[2][4], self.__board[2][5]]
        elif (boxNum == 2):
            return [self.__board[0][6], self.__board[0][7], self.__board[0][8],
                    self.__board[1][6], self.__board[1][7], self.__board[1][8],
                    self.__board[2][6], self.__board[2][7], self.__board[2][8]]
        elif (boxNum == 3):
            return [self.__board[3][0], self.__board[3][1], self.__board[3][2],
                    self.__board[4][0], self.__board[4][1], self.__board[4][2],
                    self.__board[5][0], self.__board[5][1], self.__board[5][2]]
        elif (boxNum == 4):
            return [self.__board[3][3], self.__board[3][4], self.__board[3][5],
                    self.__board[4][3], self.__board[4][4], self.__board[4][5],
                    self.__board[5][3], self.__board[5][4], self.__board[5][5]]
        elif (boxNum == 5):
            return [self.__board[3][6], self.__board[3][7], self.__board[3][8],
                    self.__board[4][6], self.__board[4][7], self.__board[4][8],
                    self.__board[5][6], self.__board[5][7], self.__board[5][8]]
        elif (boxNum == 6):
            return [self.__board[6][0], self.__board[6][1], self.__board[6][2],
                    self.__board[7][0], self.__board[7][1], self.__board[7][2],
                    self.__board[8][0], self.__board[8][1], self.__board[8][2]]
        elif (boxNum == 7):
            return [self.__board[6][3], self.__board[6][4], self.__board[6][5],
                    self.__board[7][3], self.__board[7][4], self.__board[7][5],
                    self.__board[8][3], self.__board[8][4], self.__board[8][5]]
        elif (boxNum == 8):
            return [self.__board[6][6], self.__board[6][7], self.__board[6][8],
                    self.__board[7][6], self.__board[7][7], self.__board[7][8],
                    self.__board[8][6], self.__board[8][7], self.__board[8][8]]

    # Gets the numbers of each sub grid
    def getNumsInSubGrids(self):
        numsInSubGrids = [[] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                numOfCurBox = self.__getBoxOfNum(row, col)
                numsInSubGrids.append(self.__getNumsInBox(numOfCurBox))
        return numsInSubGrids         

    def print(self):
        for i in range(9):
            if i == 0 or i == 3 or i == 6:
                print('-------------------------')  # Print top boarders
            for j in range(9):
                if j == 0 or j == 3 or j == 6:
                    print ('| ', end='')
                if j == 8:  # If last num in row, do not print space after
                    if self.__board[i][j] == None:
                        print('*', end=' |')
                    else:  # If val is num
                        print(self.__board[i][j], end=' |')
                else:
                    if self.__board[i][j] == None:
                        print('*', end=' ')
                    else:  # If val is num
                        print(self.__board[i][j], end=' ')
            print()  # Print new line if end of row
        print('-------------------------')  # Print bottom boarder
    
    # Checks if cur num is valid in its row
    def __valid_in_row(self, num, row_of_num, board):
        cur_row = board[row_of_num]  # Get row of num

        # If num is found in cur row, return false
        if num in cur_row:
            return False
        else:
            return True
        
    # Checks if cur num is valid in its col
    def __valid_in_col(self, num, col_of_num, board):
        cur_col = []
        for i in range(9):  # Get col of num
            cur_col.append(board[i][col_of_num])

        # If num is found in cur_col return false
        if num in cur_col:
            return False
        else:
            return True
        
    # Checks if cur num is valid in its box
    def __valid_in_box(self, num, rowOfNum, colOfNum, board):
        curBox = []
        boxOfNum = self.__getBoxofNum(rowOfNum, colOfNum)

        if (boxOfNum == 0):
            curBox = [board[0][0], board[0][1], board[0][2],
                       board[1][0], board[1][1], board[1][2],
                       board[2][0], board[2][1], board[2][2]]
        elif (boxOfNum == 1):
            curBox = [board[0][3], board[0][4], board[0][5],
                       board[1][3], board[1][4], board[1][5],
                       board[2][3], board[2][4], board[2][5]]
        elif (boxOfNum == 2):
            curBox = [board[0][6], board[0][7], board[0][8],
                       board[1][6], board[1][7], board[1][8],
                       board[2][6], board[2][7], board[2][8]]
        elif (boxOfNum == 3):
            curBox = [board[3][0], board[3][1], board[3][2],
                       board[4][0], board[4][1], board[4][2],
                       board[5][0], board[5][1], board[5][2]]
        elif (boxOfNum == 4):
            curBox = [board[3][3], board[3][4], board[3][5],
                       board[4][3], board[4][4], board[4][5],
                       board[5][3], board[5][4], board[5][5]]
        elif (boxOfNum == 5):
            curBox = [board[3][6], board[3][7], board[3][8],
                       board[4][6], board[4][7], board[4][8],
                       board[5][6], board[5][7], board[5][8]]
        elif (boxOfNum == 6):
            curBox = [board[6][0], board[6][1], board[6][2],
                       board[7][0], board[7][1], board[7][2],
                       board[8][0], board[8][1], board[8][2]]
        elif (boxOfNum == 7):
            curBox = [board[6][3], board[6][4], board[6][5],
                       board[7][3], board[7][4], board[7][5],
                       board[8][3], board[8][4], board[8][5]]
        elif (boxOfNum == 8):
            curBox = [board[6][6], board[6][7], board[6][8],
                       board[7][6], board[7][7], board[7][8],
                       board[8][6], board[8][7], board[8][8]]
        
        # If num is found in box, return false
        if num in curBox:
            return False
        else:
            return True

    # Checks if cur num is valid
    def __isValid(self, num, row_of_num, col_of_num, board):
        if self.__valid_in_row(num, row_of_num, board) and self.__valid_in_col(num, col_of_num, board) and self.__valid_in_box(num, row_of_num, col_of_num, board):
            return True
        else:
            return False

    # Returns true if board is solved
    def __isSolved(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == None:  # If empty space is found return false
                    return False
        return True

    # Gets indices of next empty space
    def __getNextEmptyIndices(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == None:
                    return [i, j]

    # Calls recursive function to solve board
    def solve(self):
        self.__solveRecurse(self.__board)

    # Recursively solves board
    def __solveRecurse(self, board):
        # Base case for recursion
        if self.__isSolved(board):
            self.__board = board
            return True
        
        # Get indices of next empty space
        next_empty_indices = self.__getNextEmptyIndices(board)
        cur_row = next_empty_indices[0]
        cur_col = next_empty_indices[1]

        # Try all possible nums in empty space
        for i in range(1, 10):
            if self.__isValid(i, cur_row, cur_col, board):  # If num is valid, insert it in the board
                board[cur_row][cur_col] = i
                if self.__solveRecurse(board):  # Recurse
                    return True
                else:
                    board[cur_row][cur_col] = None  # backtrack if none of possible nums are valid 

        # If no solution is found
        return False

    # API has empty tiles set to zero, so converts zeros to None
    def zerosToNone(self):
        for i in range(9):
            for j in range (9):
                if self.__board[i][j] == 0:
                    self.__board[i][j] = None