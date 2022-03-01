

#List comprehension
#List comprehension will come up on the exam. 


new_range = [i * i      for i in range(5)       if i % 2 == 0]
print (new_range)
#which corresponds to:
#"result" = ["transform"    "iteration"     "filter"]

##################################
squares = []
for n in range(10):
    squares.append(n**2)
print (squares)

#Using a list comprehension
squares = [n**2 for n in range(10)]
print(squares)

##################################
odd_squares = [n**2 for n in range(10) if n % 2 == 1]
print (odd_squares)
#This is equivalent to above
odd_squares = []
for n in range(10):
    if n % 2 == 1:
        odd_squares.append(n**2)
print (odd_squares)

#matrix is a list of lists, a list of lists is called a "matrix"

#matrix can  be used to represent seats in a "booking systems" so the list within the list is row and columns. 
matrix = [[],[],[]]
flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)

flattened = [n for row in matrix for n in row]

############################
numbers = [3, 4, 5]
doubled_odds = [] #this is known as the variable assignment 
for n in numbers: # loop line
    if n % 2 == 1: # statement line
        doubled_odds.append(n*2) #(n*2) is known as the expression

print(doubled_odds)

#this can also be represented as follows;
doubled_odds = [n*2 for n in numbers if n % 2 == 1]

print(doubled_odds)

###########################

# def stats(text):
#     unpunctuated = 

#     words =
#     num_words =