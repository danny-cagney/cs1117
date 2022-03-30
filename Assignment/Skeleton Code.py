#Name:
#Student ID:
#Programme:

########################## Question 1a ############################################
def encrypt(w):

    vowels = {'a':0, 'e':1, 'i':2, 'o':2, 'u':3}

    '''Step 1 reverse the input e.g. if w is 'apple', it should be 'elppa' '''
    #Your code here

    '''Step 2 Replace all vowels using the dictionary provided e.g. elppa becomes 1lpp0 '''
    #Your code here

    '''Step 3 Add 'a5a' to the end of w e.g. 1lpp0a5a '''
    #Your code here

    return w   #output should be 1lpp0a5a for an input of apple

word = input("Enter a single word: ")
encryptedWord = encrypt(word)
print (encryptedWord)

########################## Question 1b ############################################

def frame(width, height, character):
    #Your code goes here
    
    if width <= 2 or height <= 2:
        print ("Invalid")
        exit()
    else:
        print( character * width)
        for rowNumber in range(height):
            print(character, end='')
            print(" " * (width-2), end='')
            print(character, end='')
        print (character * width)
    print(frame)

width = int(input("Enter the width of the frame: "))
height = int(input("Enter the height of the frame: "))
character = input("Enter the character: ")
frame(width, height, character)

########################## Question 1c ############################################

# WHILE LOOP

def someFunction (L1):
    newList = []
    length = len(L1)
    counter = 0
    while counter < length:
        if L1[counter] > 5:
            newList.append(L1[counter])
        counter += 1
    return newList

# FOR LOOP 

    for counter in range(length):
        if L1[counter] > 5:
            newList.append(L1[counter])

def someListCompFunc (L1):
    
    newList = [L1[counter] for counter in range(len(L1)) if L1[counter] > 5 ]
#Your code here to rewrite with for loop - test
#Your code here to rewrite with as list comprehension - test

print(someFunction([3, 4, 15, 7, 5, 6, 7]))

########################## Question 1d ############################################
def totalEvenlyDivides (start, stop, divisor):
    #Your code here

    return total

print (totalEvenlyDivides(1, 10, 2)) 
print (totalEvenlyDivides(1, 10, 3))
print (totalEvenlyDivides(2, 6, 25)) 

########################## Question 2 ############################################
def calculate_score (board):

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
    rowTotals = []
    colTotals = []

    '''Calculate the score per row and append it to the rowTotals list'''
    #Your code goes here

    '''Calculate the score per column and append it to the colTotals list'''
    #Your code goes here

    return rowTotals, colTotals

rTotals, cTotals = calculate_score([["#", "!"],["!!", "X"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]])
print (rTotals, cTotals)
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

########################## Question 3 ############################################
def read_file (input_file):
    Users = {}
    #Your code goes here
    return Users

print(read_file ("details.txt"))

########################## Question 4 ############################################
def identifyPivot (L):
    #Your code goes here
    
    pivot = -1

    leftSidePivotSum = 0
    rightSidePivotSum = 0


    for i in range ( 1, (len (L))):
        rightSidePivotSum += L[i]

    while 

    if leftSidePivotSum == rightSidePivotSum:

    else:
        return pivot

print(identifyPivot([9,1,9])) #returns 1
print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0