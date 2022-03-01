
def readFile (filename):
    #read the file and return a list of words. 

def depunctuate (words):
    punctuation = [",", ".", "!", "?", "-", "'"]
    #depunctuate the words and return a cleaned list

def countWords (words):
    #create a dictionary
    #if a word doesn't exist add it as a key with 1 as a value
    #it it does exist add 1 to the current count
        
    #process the dictionary to see which word has the highest count.
    #keep track of the highest word and associated count

    #write this to an output file

#Main Program:

#read in the file to get a list of words (best use a function)
words_text = readFile("books.txt")

#depunctuate the lists of words
words_cleaned = depunctuate(words_text)

#count the words, calculate the max and write to a file
countWords(words_cleaned)