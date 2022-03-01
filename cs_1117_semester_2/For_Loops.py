#For Loops ---> Mutable data such as list or string

name = "Daniel"

#Type 1: Get item in an iterable data structure. 
for letter in name:
    #do something
    print(letter + "*")

#Type 2: range(start, stop, step)
for index in range(0, 10, 1): # 10 goes as far as 10 but not including 10
    #do something
    print(index)

#Type 2: Get you an index or number, and you are using the index to get the item
for index in range(len(name)):
    #do something
    print(name[index] + "*")

#Type 3: Get both. You get the item and you get the index
for index, letter in enumerate(name):
    print(index, letter)

#Method 1
salaries = [30000, 40000, 50000]

for salary in salaries:
    print (salary)

for i in range(len(salaries)):
    print (i)

#Nested loops is like an analog clock.
#The minute hand moves 60 times for each movement of the hour hand. 
#So for each iteration of hours do 60 iterations of minute

for num1 in range(3):
    for num2 in range(2):
        print (num1+num2)

for i in range():
    print (i)


