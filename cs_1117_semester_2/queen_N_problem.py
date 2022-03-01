# BACKTRACKING ALGORITHM:
'''The idea is to place queens one by one in different columns, starting from the 
leftmost column.
When we place a queen in a column, we check for clashes with already placed queens.
In the current column, if we find a row for which there is no clash, we mark this 
row and column as part of the solution.
If we do not find such a row due to clashes then we backtrack and return false.'''
# Great video on website: https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/
# Brute Force: https://en.wikipedia.org/wiki/Eight_queens_puzzle
# PSEUDOCODE
'''
1) Start in the leftmost column
2) If all queens are placed - you know this because the column number will exceed 
the size of the board.
   You wouldn't get this far unless the queens are placed correctly. 
    return the solved board and True. This is the base case. 
3) Otherwise, try all rows in the current column.  Do the following for every tried
row.
    a) If the queen can be placed safely in this row then mark this [row, 
        column] as part of the solution and recursively check if placing  
        queen here leads to a solution. This is the recursive case. 
    b) If placing queen in [row, column] leads to a solution then return 
        the solved board and True.
    c) If placing queen doesn't lead to a solution then mark this [row, 
        column] i.e. put it back to 0. (Backtrack) and go to step (a) to try other 
rows.
3) If all rows have been tried and nothing worked, return false to trigger 
    backtracking.
'''
def createBoard(n):
    b = []
    for numberOfRows in range(n):
        row = []
        for numOfCols in range (n):
            row.append(0)
        b.append(row)
    return b

def printBoard(SBoard):
    for i in range (len(SBoard)):
        for j in range (len(SBoard)):
            print (SBoard[i][j], end=" ")
        print ("\n")


def isValidMove(board, row, col): 
# Check this row on left side
    for colNo in range(col):                #colNo could be anything for example 'i'
        if board [row][colNo] == 1 :        #queen already in the row.
            return False

# Check upper diagonal on left side 
    for rowNo, colNo in zip(range(row, -1, -1), range(col, -1, -1)):
        if board [row][colNo] == 1 :        #queen already in the row.
            return False

# Check lower diagonal on left side         increment the row till the end of the board, decrement the col till end 
    for rowNo, colNo in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board [row][colNo] == 1 :        #queen already in the row.
            return False
    #return true/false
    return True


def solveBoard(b, col):
    #base case:
    if col == n:
        return b, True         #pass back the completed board(b) and True
    for row in range(n):
        if isValidMove(b, row, col) == True:
            b[row][col] = 1     #place the queen
       
            b, answer = solveBoard(b, col + 1)
            if answer == True:
                return b, True
            b[row][col] = 0
       
        else:
            #recursive case:
            b = solveBoard(b, col + 1)
            
    return b, False

def printBoard(SBoard):
    for i in range(len(SBoard)):
        for j in range(len(SBoard)):
            print(SBoard[i][j], end=" ")
        print("\n")


# Main Program
n = int(input("What is the width of the board?"))

board = createBoard(n)

solvedBoard, result = solveBoard(board, 0) #pass in the empty board (matrix) and the column to start at i.e. the first column with index 0

if result == False:

    print("Solution does not exist")    # n = 2 & N = 3 won't work....

else:

    printBoard(solvedBoard)             # printBoard (board)