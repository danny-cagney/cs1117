
#{} - dictionary
#[] - list, list slicing / string slicing
#() - tuple, defining function definition

#Structure of a dictionary
from re import M


myDictionary = {"Mary": 2, "John": 2, "Adam": 1}

#Create an item or entry into a dictionary
#syntax: dictionaryNmae[key] = value

myDictionary ["Jenny"] = 6
print (myDictionary)


#Look up something in the dictionary
#e.g. How many modules is Jenny taking?
numModules = myDictionary["Jenny"]

#Overwrite / update a value in the dictionary
myDictionary["Jenny"] = myDictionary["Jenny"] + 1 #long hand version
myDictionary["Jenny"] += 1 #short hand version

#Using the in-built methods .keys(), .values(), .items()
myDictionary.keys()
names = myDictionary.keys()

for name in myDictionary.keys():
    print (myDictionary[name])    #print values
    print (name)     

for name in names:
    print (name)

totalModules = 0
for numModules in myDictionary.values():
    totalModules += numModules
print (totalModules)

print (myDictionary.items())

for student in myDictionary.items():        #NB this gives you back a list of tuples
    if student == "Mary":
        print ("do something something")

