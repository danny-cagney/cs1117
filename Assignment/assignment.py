# #Name: Daniel Cagney
# #Student ID: 121707785
# #Programme: CK401 - BSc Year 1 - CompSci

# ########################## Question 1 ############################################

# """Question 1: 
# Remember to comment your solution with logical comments and comments describing the 
# programming constructs. This will be weighted heavily.  
# See the skeleton code relating to this question. A matrix (list of lists) containing different symbols is 
# input into a function called calculate_score. The function should calculate various scores 
# according to the provided symbols dictionary.  
# symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5} 
 
# Specifically, it must calculate: 
# • The score per row and put in a list called rowTotals 
# • The score per column and put in a list called colTotals. 
# rowTotals and colTotals are then returned from the function and printed to the screen.   
# If any of the final row scores or column scores are negative, a zero (0) should instead be appended 
# to the list.  
# e.g.  
# A list containing a !!!, 2 #’s and an X would equal (-5 + 5 + 5 + 1) = 6 so would append 6 to the list.  
# A list containing a !! and an X would equal (-3 + 1) = -2 so would append 0 to the list. 
# The function returns the list of row totals and the list of column totals.  
# Sample Output: 

# """
 
 
 






# def calculate_score (board):
#     symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
#     '''Calculate the score per row and append it to the rowTotals list'''
#     #Your code goes here
#     '''Calculate the score per column and append it to the colTotals list'''
#     #Your code goes here
#     return rowTotals, colTotals

# rTotals, cTotals = calculate_score([["#", "!"],["!!", "X"]])

# print (rTotals, cTotals)

# rTotals, cTotals = calculate_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]])

# print (rTotals, cTotals)






# rTotals, cTotals = calculate_score([
#   ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
#   ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
#   ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
#   ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
#   ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
#   ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", 
# "!!!"],
#   ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
#   ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
#   ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
#   ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
#   ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
#   ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
#   ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", 
# "#"],
#   ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]])
# print (rTotals, cTotals)




# ########################## Question 2 ############################################


# """Question 2: 
# Remember to comment your solution with logical comments and comments describing the 
# programming constructs. 
# This will be weighted heavily.  
# See the skeleton code relating to this question. 
# Write the function identifyPivot that takes a list as input and output the number that is the pivot.  
# If there is no pivot, -1 should be returned. 
# If there are multiple pivot numbers in a single list, return the first one that occurs. 

# Example: 
# identifyPivot([9,1,9]) returns 1 
# identifyPivot ([8,8,8,8]) returns -1 
# identifyPivot ([1,2,4,9,10,-10,-9,3]) returns 4 
# identifyPivot ([7,-1,0,-1,1,1,2,3]) returns 0 """




# # def identifyPivot (L):
# #     #Your code goes here
# #     pivot = ''
# #     return pivot


# print(identifyPivot([9,1,9])) #returns 1
# print(identifyPivot ([8,8,8,8])) #returns -1
# print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
# print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0

# Python 3 Program to find an element
# such that sum of right side element
# is equal to sum of left side
 
# Function to compute partition
def identifyPivot(L):
    """The pivot point of a list is a number where all the numbers to the left of it 
    and all the numbers to the right of it sum to the same value.
    - initialise rightside sum
    - initialise leftside sum
    - if the leftside sum == rightside sum, then return the number form the list at the index
    - if there is no pivot index to return then the function returns -1
    """

    rightSideSum = 0 #initialise a variable that will be used to calculate sum on right side of the pivot point.
    leftSideSum = 0 #initialise a variable that will be used to calculate sum on left side of the pivot point.

    listLength = len(L) #initialise a variable that will require a function will need the 
 
    # Computing right_sum
    for i in range(1, listLength): #establish a loop that will 
        rightSideSum += L[i]
 
    i = 0

    j = 1
 
    # Checking the point of partition
    # i.e. left_Sum == right_sum
    while j < listLength:
        
        rightSideSum -= L[j]
        
        leftSideSum += L[i]
 
        if leftSideSum == rightSideSum:
            return L[i + 1]
 
        j += 1
        i += 1
 
    else:
        return -1
 
     


print(identifyPivot([9,1,9])) #returns 1
print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0

