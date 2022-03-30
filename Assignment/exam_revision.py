
vowels = {'a':0, 'e':1, 'i':2, 'o':2, 'u':3}

word = 'apple'

word = word[::-1] # reverse a string using string slicing. 



#alternative way to do this
# word = list(word)
# word.reverse()
# word = "".join(word)
# print (word)

for c in word:
    if c in vowels: #.keys, .values, .items - for dict methods 
        word.replace(c, str(vowels[c])) # we must cast the 'vowels[c]' because the data type coming from the dict is an integer.
    


# encryptedWord = ''

# for c in word:
#     if c in vowels: 
#         encryptedWord += vowels[c]
#     else:
#         encryptedWord += c

# encryptedWord = (encryptedWord + "a5a")

print (word)



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