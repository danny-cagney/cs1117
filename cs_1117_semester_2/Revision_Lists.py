#List: an object that can contain anything / multiple data types

student = ["Mary", "Murphy", 20]
print (student[1])

fnames = ["Mary", "John"]
lnames = ["Murphy", "OSullivan"]

students = [fnames, lnames]

for student in students:
    for firstname in students[0]:
        print (student)


#Index Error exception is raised if an invalid index is used
#(stop in range command is incorrect)


numbers = [12, 14, 15]
userNumber = 13

if userNumber in numbers:
    print ("Yes")
else:
    print ("No")

#Processing a List 

shopping = [34, 57, 46, 89]
totalSpend = 0

for shop in shopping:
    totalSpend += shop

    print (totalSpend)

myList = [10, 20, 30]

index = 0

while index < len(myList):
    print(myList[index])
    index += 1

for index in range(len(myList)):
    print (myList[index])