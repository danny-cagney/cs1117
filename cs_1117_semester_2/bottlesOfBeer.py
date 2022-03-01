"""Write a function called bottlesOfBeer() that accepts an input argument 
numberOfBottles. The function displays to the screen the lyrics for a popular repetitive 
song e.g. “99 bottles of beer on the wall, 99 bottles of beer. Take one down, pass it 
around, 98 bottles of beer on the wall”. The same lyric is always repeated, each time 
with one less bottle. The song is completed when the singer reaches 0. Use the proper 
inflection for “bottle” instead of “bottles” (Hint: this may require an if-elif-else 
statement). Example output: """

def bottlesOfBeer():
    """This function accepts argument as user input. Parameter passed by user is the number of bottles remaining on the wall.
    - Words of the song repeat until no bottles of beer are left on the wall.
    - Function uses a while loop which decrements on each iteration."""
    
    #Argument is passed in by user and stored in variable 
    numberOfBottles = int(input("Enter number of bottles:"))

    #while loop condition
    while numberOfBottles > 0:
        #while loop body
        if numberOfBottles > 1:
            print (f'{numberOfBottles} bottles of beer on the wall, {numberOfBottles} bottles of beer. Take one down, pass it around,', (numberOfBottles - 1), 'bottles of beer on the wall')
        
        elif numberOfBottles == 1:
            print (f'{numberOfBottles} bottle of beer on the wall, {numberOfBottles} bottle of beer. Take one down, pass it around,', (numberOfBottles - 1), 'bottles of beer on the wall')
        
        #The loop is decremented by (1) on each iteration of the loop.
        numberOfBottles -=1

bottlesOfBeer()