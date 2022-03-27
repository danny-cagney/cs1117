


clues = [[34, 21, 32, 41, 25], [14, 42, 43, 14, 31], [54, 45, 52, 42, 23], [33, 15,
51, 31, 35], [21, 52, 33, 13, 23]]

def checkTreasure (clue, row, col):
    """check if the coordinates is the same as the clue.  e.g. first iteration: if 34 == 11:
    #if it is return true, if not return false. """
    

    coords = int(str(row) + str(col)) #we are casting from strings back to ints, back to string

    if clue == coords:
        found = True
    else:
        found = False
        print(clue)

    return found

#start up the top left - get the clue i.e. 34
#get the coordinates i.e. the row number
#get the coordinates i.e. the column
#check if the treasure is found by calling the checkTreasure function which returns 
# a if:
#     return True or 
# #     Else:
# #     return False

clue = clues[0][0]
row = 1
col = 1

found = checkTreasure(clue, row, col)

while found == False:
    #get the new row number
    row = int(str(clue)[0])
    #get the new column number
    col = int(str(clue)[1])
    #get the new clue
    clue = clues[row -1][col - 1] #instead of [3,4]....it's [2,3]
    #check if this is the treasure
    found = checkTreasure(clue, row, col)

print("yippee, treasure found.")
print(clue, row, col)