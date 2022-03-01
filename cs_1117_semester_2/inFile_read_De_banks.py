inFile = open("debanks.txt", "r")

#read
lyric = inFile.readline()

# while lyric != "":
#     print(lyric)            #Do I need to strip out the \n character
#     lyric = inFile.readline()
#     lyric = inFile.read()
#     lyric = inFile.readlines()

for lyric in inFile:
    print (lyric)

print (lyric)

inFile.close()