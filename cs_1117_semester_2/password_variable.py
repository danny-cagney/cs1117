# i = 0                           #i is the index variable

# while i < 5:
#     print ("i'm in the loop")   # must have control variable must be in the while loop to make the statement false
#     i = i + 1  #i+=1            # = is the assignment operator


# condition = False

# while condition == False:       #(while not condition, is defaulting to false), (while condition is defaulting to true)
#     print ("do something")

#     if something:
#         condition = True


def createPassword ():
    '''Check if length is at least 8
    Print error message if not
    If at least 8 then carry on to count
    Number of digits
    Number of upper case letters
    Number of lower case letters
    Check there is at least 1 digit, 1 uppercase letter and 1 lowercase letter'''

    ok = False

    while not ok:   #same as saying while ok == False

        password = input ('Please enter a password >>>')

        if len(password) < 8:
            print ('Not a valid password')
        
        else:
            i = 0       # control variable for my while loop
            upper = 0   # counter 
            lower = 0
            digit = 0

            while i < len(password):
                if password[i].isupper():
                    upper +=1

                elif password[i].islower():
                    lower +=1

                elif password[i].isdigit():
                    digit +=1

                i += i

            # if (upper >= 1 and lower >=1 and digit >=1) == True:
            #         ok = True
            ok = upper >= 1 and lower >=1 and digit >=1

            if not ok:
                print ('This is the wrong combination ')
                
    print ("Your password is: ", password)

    


