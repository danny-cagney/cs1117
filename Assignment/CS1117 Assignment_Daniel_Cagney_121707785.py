#Name: Daniel Cagney
#Student ID: 121707785
#Programme: CK401 - BSc Year 1 - CompSci

############################## Question 1 ############################################

def calculate_score (board):
    """
    - This function takes an input of a list of lists. The matrix is lists of various symbols.
    - These symbols have associated values. The values are contained within a dictionary called "symbols".
    - We access a dictionary called {symbols}, which contains numerical values, for the various symbols.
    - Function calculates the numerical totals, for each row.
    - Function calculates the numerical totals, for each column.
    - Calling this function returns rTotals, cTotals
    """

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}

    rTotals = [] #initialise an empty list. This list will be a 2D matrix that contains lists of the row totals.
    
    for rowNo in range(len(board[0])): #this is an outer loop, which iterates over the number of elements in that list. In this example we can pick any index, picking index 0 to setup the condition for the for-loop, adding the numerical value from symbols dict, for each item in the row / list 
        
        rowTotal = 0 #we need to initialise a row total, before the inner loop, but inside the outer loop, so that the value will be reset after each iteration, but wont be cumalative, if the variable was setup outside of both loops.
       
        for colNo in range(len(board)): #Using a nested loop, the inner loop runs through each element in the list. #keeping the row steady for each iteration of the outer loops, and changing the column for each of the inner loops.
            rowTotal += symbols[board[rowNo][colNo]] # to access the 'symbols' dict, we need to include the variable names, the data, and the colNo and RowNo, as the key to access the value at that key.
 
        if rowTotal < 0: #if the rowtotal is less than 0 i.e. a negative integer, we discount the negative value and give the row total a value of 0. 
            rowTotal = 0 #then the row total is ready to append to the matrix, which is going to be [0]

        rTotals.append([rowTotal]) #Using the list method (append) we append a list of the row total, it is appended to the already initialised 'rTotals' variable.

# '''Calculate the score per column and append it to the colTotals list'''
# A similar process can be used for totalling the column totals, with some config of the order in which the loops iterates and acccesses the lists.

    cTotals = [] #initialise a variable that will contain a matrix, or a list of list. 
    
    for colNo in range(len(board[0])): #we need index[0] is used an arbitrary reference. As this is a 14 x 14 board i.e. 14 elements in each of the 14 lists we can use the arbitrary index [0]
        
        colTotal = 0 #initialise a single column total, inside the first for loop.
        
        for rowNo in range(len(board)): #Using a nested loop, the inner loop runs through each element in the list. #keeping the column steady for each iteration of the outer loops, and changing the row for each of the inner loops.
            colTotal += symbols[board[rowNo][colNo]] #keeping the col steady for each iteration of the outer loops, and changing the row for each of the inner loops.
        if colTotal < 0: #Using an IF statement, checking if the single column total is less than 0 i.e. a negative integer, we discount the negative value and give the column total a value of 0. 
            colTotal = 0 #then the col total is ready to append to the matrix, and its value is going to be "0"

        cTotals.append([colTotal]) #Using the list method.append, we append a list of the column total, this list is appended to the already initialised cTotals variable

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

print (rTotals, cTotals)


################################## Question 2 ############################################


def identifyPivot(L): #this function takes one argument, i.e.list input
    """The pivot point of a list is a number where all the numbers to the left of it and all the numbers to the right of it sum to the same value.
    - initialise rightside sum to 0, outside of any loops as we will adjust the total Sum with each iteration.
    - initialise leftside sum to 0, outside of any loops as we will adjust the total Sum with each iteration.
    - if the leftside sum == rightside sum, then return the number form the list at the index
    - if there is no pivot index to return then the function returns -1
    - where the left side of the sum equals the right side of the sum, we can find the index at which lies between these two equal sums. 
    - This function returns the value at the index which is the pivot point, else it returns (-1)
    """
    pivot = -1
    # we will need to initialise two variables that will contain the total sum values for the left side sum total and the right sum total. 
    rightSidePivotSum = 0 #we need to initialise a variable that will store the value of the sum of all numbers to the right of the pivot index being checked. That is, we calculate sum on right side of the pivot point.
    
    #we need to initialise a variable that will be used to calculate and store the total sum on left side of the pivot point, as we iterate through he list indices.
    leftSidePivotSum = 0 

 
    # I use a for loop to iterate over the list, using the range command, so as to start the iteration at index[1], to run through to the length of the list. 
    for i in range(1, len(L)): #we must begin somewhere in the list to start checking, it is logical to start on the left side, therefore I have selected the left side of the list, working from left most number through to the right most number in the list.
        # assuming we start on the left side of the list, we establish a loop that will that will not start at index [0], as this can not be a pivot point. Hence, the range command starts at 1, thus skipping the first index (i.e index[0]
        rightSidePivotSum += L[i] #this adds all the numbers in the list, (except for the first number at index[0])
       

    initialIndex = 0 #initialise variable as the index which we access the list of numbers with. 
    # This will be used to add to the sum totals later. 
    # We initialise to 0, because we have made an assumption to start on the left side of the list. As the left most index cannot be a pivot then index[1] must be the first possible pivot.
    # and work through the list at the start working from left to right. This will be used to access the values in the list, add to the sum totals later. 
    checkIfPivotIndex = 1 #initialise a pivot index (first pivot point to check) check index of list. This will be used to access the values in the list, add to the sum totals later. This is the first possible index at which the pivot point maybe. 
 
    # summing sides and checking the pivot point
    # i.e. checking that the left side of the pivot point sum is equal to the right side of the pivot point sum.
    
    while checkIfPivotIndex < len(L): # we use a while loop here as we DO NOT know how many iterations of the list will be required to find the pivot point.
        # the condition we apply on the while loop is to iterate while the index number being checked is less than the length of the list, so as the loop does not continue in defintely. 
        
        rightSidePivotSum -= L[checkIfPivotIndex] #decrement - we need to remove the number at the index being checked, from the total sum value of the right hand side of the sum, as it is not included.
        leftSidePivotSum += L[initialIndex] #increment - we now need to increase the sum value stored in this variable to take account that the next index in the list is being checked, 

        # in order to return the number at the "pivot" index, we need to check that the,
        # sum on the left of the pivot is equal to the sum of the numbers on the right side.
        if leftSidePivotSum == rightSidePivotSum:
            
            return L[checkIfPivotIndex] #if the right side of the sum and left side of the sum are equal, 
            #we can return the value / number at the list[index] that we are checking i.e. list_index[index being checked as the pivot point].

        #otherwise, we now need to increase the index of the list, and of the index being checked which we are checking on each iteration of the while loop.
        checkIfPivotIndex += 1 #increment the checkPivotIndex, if the left side sum does not equal right side sum.
        initialIndex += 1 #increment the initial index, so that during the next iteration we can add the next number value at that index, to the right at the index, to the left side total of the sum. 

    else:
        return pivot #if there is no pivot index identified, then we should return -1 as per the question outline.
 
print(identifyPivot([9,1,9])) #returns 1
print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0
print(identifyPivot ([1,2,3,4,5,10,20,-5])) #returns 10
print(identifyPivot ([20, 20, 20, 20, 20, 1, 100])) #returns 1
print(identifyPivot ([100, 1, 20, 20, 20, 20, 20])) #returns 1

 