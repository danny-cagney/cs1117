inFile = open ("debanks.txt", "r")
outFile = open ("song.txt", "w")

#Method 1: Using the Python file iterator
lineNo = 1
for line in inFile:
    #print (str(lineNo) + ": " + line)
    outputLine = str(lineNo) + " - " + str(len(line)) + " - " + line
    print (outputLine)
    outFile.write(outputLine)
    lineNo += 1

#Method 2: Use the readLine method - reads ONE line, includes \n character, empty string when it reaches the end of the file
#line = inFile.readline()
#lineNo = 1
#while line != "":   #as long as you haven't reached the end of the file
#    print (str(lineNo) + ": " + line)
#    line = inFile.readline()
#    lineNo += 1

#Method 3: Use the read() method - Reads the ENTIRE file as ONE string. 
#entireFile = inFile.read()
#lines = entireFile.split("\n")      #gives me back a list of the lines
#lineNo = 1
#for line in lines:
#    print (str(lineNo) + ": " + line)
#    lineNo += 1

#for lineNo in range (len(lines)):
#    print (str(lineNo + 1) + ": " + lines[lineNo])

#Method 4: Use the readLines() method: gives you back a list of lines
#lines = inFile.readlines()
#lineNo = 1
#for line in lines:
#    print (str(lineNo) + ": " + line)
#    lineNo += 1

inFile.close()
outFile.close()