"""Question 1: 
Assume you have a file called lotteryNumbers.txt. This contains the winning lottery draws (6 
numbers for each draw) for the last year, with each draw on a separate line and the numbers 
separated by a single space. Example: 
 
23 30 5 8 18 14 
11 10 3 17 18 20"""

"""Write a function called readDraws() to read this file into a list called lotteryDraws. Each draw within 
this list should be a list of integers. This function should return a list of the of the integer lottery 
numbers e.g. [[23, 30, 5, 8, 18, 14], [11, 10, 3, 17, 18, 20], .....] 

Write a function called checkWinners (lotteryDraws) that asks the user to enter their lotto numbers 
and checks if they are winners. Assume the users enters the correct amount of numbers with a 
space between each number. They are only considered to be a winner if they have all 6 numbers 
within the same draw. We do not consider partial wins i.e. 5 numbers within a draw etc. You can use 
the inbuilt sort function to sort the list if you wish. The function should return a message “You have 
won!” if there is a match and “Better luck next time” if not. """

def readDraws(filename):
    
    lotteryDraws = []
    lotteryDraws += lotteryDraws.append()
    return lotteryDraws




def checkWinners(lotteryDraws):
    userLottoNumbers = []
    while len(userLottoNumbers) < 6:
    
        LottoNumber = int(input("Please enter your lotto number "))

        if LottoNumber not in userLottoNumbers and LottoNumber < 42 and LottoNumber > 0:
            userLottoNumbers.append(LottoNumber)
            userLottoNumbers.sort()  
            print (userLottoNumbers)

            if LottoNumber > 42 or LottoNumber < 1:
                print("Your number is outside range, please pick another number between 1 and 42")

            elif LottoNumber in userLottoNumbers:
                print("Number already chosen, please pick another")
        
            elif LottoNumber > 42 or LottoNumber < 1:
                print("Your number is outside range, please pick another number between 1 and 42")

            elif LottoNumber in userLottoNumbers:
                print("Number already chosen, please pick another")
    
    return userLottoNumbers
    
    # while len(userLottoNumbers) < 6:
    #     LottoNumber = int(input("Please enter your "))
    #     


    # return

    # if:
    #     return "You have won!”
    # else:
    #     return "Better luck next time”
