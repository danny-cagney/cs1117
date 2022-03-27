stepData = [[9000, 10000, 10000, 11100, 3400], [2000, 2000, 3400, 5400, 12300], 
[11000, 12000, 13435, 11234, 10347], [9800, 9500, 8900, 10002, 10054], [4500, 5697,
7898, 8796, 10324], [7600, 12000, 12345, 11234, 9820], [13560, 14000, 13000, 11000,
10986], [7600, 4356, 9820, 10980, 11240], [10005, 11112, 12243, 13354, 9002], 
[10340, 10546, 10890, 10002, 9002]]
#(a) The number of week-days on which at least 100,000 steps were made cumulatively by all employees i.e. Add Columns.

numWeekdays = 0

for col in range (len(board[0])):
    weekdayTotal = 0
    for row in range(len(board)):
        weekdayTotal += board [row][col]
        if number < 0:
            numWeekdays += 0

print ("Number of weekdays over 100000: ", numWeekdays) 
#(b) The number of the employee who took the most steps in the week (assume there can only be one). i.e. add the row and check for max

symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}

rowTotal = 0
rowTotals = []

def find_row_total(board):
    for symbol in range (len(board)):
        number = symbols[symbol]
        rowTtotal = 0
        for step in employee:
            rowTotal += number

#print (employeeID, total)
    if total > employeeMostSteps:
        employeeMostSteps = total
        employeeMostStepsID = employeeID

print("Employee ID with most steps is: ", employeeMostStepsID, "with", employeeMostSteps, "steps")