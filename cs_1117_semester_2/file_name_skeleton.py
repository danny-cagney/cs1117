file_name = "whatever.txt"

#(1) Must "open before use"
textfile = open(file_name, "r") #The variable 'textfile' points to a file object

# r - read in from a file. Choose a suitable variable name such as inFile
# w - write out to file. If it does not exist, create one. Choose a suitable variable name such as outFile
# a - append - Assumes the file exists and you want to read onto the end of the file


#(2) Read through the file from the beginning to end




#(3) "close" when done
textfile.close()            




# f.readline() - readline reads a single line(as a string, including newline (\n) character);
#empty string signifies end of file. Generally in conjunction with loop.

# f.read() - read devours entire file and returns contents as a single string.

# f.readlines() - readlines devours entire file and returns contents as list of lines (strings)

