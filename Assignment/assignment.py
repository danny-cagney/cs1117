#Name: Daniel Cagney
#Student ID: 121707785
#Programme: CK401 - BSc Year 1 - CompSci

############################## Question 1 ############################################

def calculate_score (board):
    """
    - This function takes an input of a list of lists. The matrix is lists of symbols.
    - These symbols have associated values. We access a dictionary called {symbols}, 
    - which contains numerical values, for the various symbols
    - Function calculates the numerical totals, for each row.
    - Function calculates the numerical totals, for each column.
    - Calling this function returns rTotals, cTotals
    """

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}

    rTotals = [] #initialise an empty list. This list will be a 2D matrix that contains a lists of the row totals.
    
    for rowNo in range(len(board[0])): #this is an outer loop, which iterates over each row, adding the numerical value from symbols dict, for each item in the row / list 
        
        rowTotal = 0 #we need to initialise a row total, before the inner loop so that the value will be reset after each iteration.
       
        for colNo in range(len(board)): #inner loop runs through each element in the list. #keeping the row steady for each iteration of the outer loops, and changing the column for each of the inner loops.
            rowTotal += symbols[board[rowNo][colNo]]
 
        if rowTotal < 0: #if the total of the 
            rowTotal = 0 #then the col total to append to the matrix is going to be [0]

        rTotals.append([rowTotal]) #append a list of the row total, append to the initialised rTotals variable

#     '''Calculate the score per column and append it to the colTotals list'''

    cTotals = [] #initialise a variable that will contain a matrix, 
    
    for colNo in range(len(board[0])): #we need index[0] is used an arbitary reference 
        
        colTotal = 0 #initialise a single column total, inside the first for loop.
        
        for rowNo in range(len(board)): 
            colTotal += symbols[board[rowNo][colNo]] #keeping the col steady for each iteration of the outer loops, and changing the row for each of the inner loops.
        if colTotal < 0: #if the total of the 
            colTotal = 0 #then the col total to append to the matrix is going to be "0"

        cTotals.append([colTotal]) #append a list of the column total, append to the initialised cTotals variable

    return rTotals, cTotals #the calculations are complete and the function then returns the Row totals, and the Column totals.


##############################################################

# print (rTotals, cTotals)
rTotals, cTotals = calculate_score([
["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"], 
["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]])

#print (rTotals, cTotals)


################################## Question 2 ############################################

 
# Function to compute partition
def identifyPivot(L):
    """The pivot point of a list is a number where all the numbers to the left of it and all the numbers to the right of it sum to the same value.
    - initialise rightside sum to 0, outside of any loops as we will adjust the total Sum with each iteration.
    - initialise leftside sum to 0, outside of any loops as we will adjust the total Sum with each iteration.
    - if the leftside sum == rightside sum, then return the number form the list at the index
    - if there is no pivot index to return then the function returns -1
    - where the left side of the sum equals the right side of the sum, 
    we can find the index at which lies between these two equal sums. 
    """

    rightSidePivotSum = 0 #we need to initialise a variable that will store the value of the sum of all numbers to the right of the pivot index being checked. That is, we calculate sum on right side of the pivot point.
    leftSidePivotSum = 0 #we need to initialise a variable that will be used to calculate and store the total sum on left side of the pivot point, as we iterate through he list indices.

 
    # I use a for loop to iterate over the list, using the range command, so as to start the iteration at index[1], to run through to the length of the list. 
    for i in range(1, len(L)): #we must begin somewhere, therefore I have selected the left side of the list, 
        # assume establish a loop that will. Hence, the range starts at 1, thus skipping the first index avoid the 
        rightSidePivotSum += L[i] #this adds all the numbers in the list, (except for the first number at index[0])
        # print ("right side sum:", rightSidePivotSum)

    initialIndex = 0 #initialise variable as the index which we access the list of numbers with. 
    # This will be used to add to the sum totals later. 
    # We initialise to 0, because we have made an assumption to start on the left side of the list. As the left most index cannot be a pivot then index[1] must be the first possible pivot.
    # and work through the list at the start working from left to right.
    checkPivotIndex = 1 #initialise a pivot index (first pivot point to check) check index of list. This will be used to add to the sum totals later. This is the first possible index at which the pivot point maybe. 
 
    # summing sides and checking the pivot point
    # i.e. checking that the left side of the pivot point sum is equal to the right side of the pivot point sum.
    
    while checkPivotIndex < len(L): # we use a while loop here as we DO NOT know how many iterations of the list will be required to find the pivot point.
        # the condition we apply on the while loop is to iterate while the index number being checked is less than the length of the list. 
        
        rightSidePivotSum -= L[checkPivotIndex] #decrement - we need to remove the number at the index being checked, from the total sum value of the right hand side of the sum.
        leftSidePivotSum += L[initialIndex] #increment - we now need to increase the sum value stored in this variable to take account  the 

        # in order to return the number at the "pivot" index, we need to check that the,
        # sum on the left of the pivot is equal to the sum of the numbers on the right side.
        if leftSidePivotSum == rightSidePivotSum:

            return L[checkPivotIndex] #if the right side of the sum and left side of the sum are equal, 
            #we can return the value / number at the list[index] that we are checking i.e. list_index[index being checked as the pivot].

        #otherwise, we now need to increase the index of the list, of the index being checked which we are checking
        checkPivotIndex += 1 #increment the checkPivotIndex, if the left side sum
        initialIndex += 1 #increment the initial index, so that during the next iteration we can add the next number to the right at the index, to the left side total of the sum. 

    else:
        return -1 #if there is no pivot index identified, then we should return -1 as per the question outline.
 
print(identifyPivot([9,1,9])) #returns 1
print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0
print(identifyPivot ([1,2,3,4,5,10,20,-5])) #returns 10
print(identifyPivot ([20, 20, 20, 20, 20, 1, 100])) #returns 1

 