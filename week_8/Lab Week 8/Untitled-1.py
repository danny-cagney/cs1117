#Question 1
from multiprocessing.connection import answer_challenge
from operator import truediv


programming_languages = ('php','java','python','c++','c') 

"""

• Use map and lambda to convert these programming languages to upper case in a single 
line of code using map and lambda. Print out the tuple to confirm correct operation. 
• Now rewrite this to use a list comprehension. 
• Now re-write this to use traditional code i.e. loop and list.

"""

upper = map(lambda x : x.upper(), programming_languages)
upper = list(upper)
print (upper)

programming_languages_list_upper = list(map(lambda x : x.upper(), programming_languages))
print (programming_languages_list_upper)

programming_languages = ('php','java','python','c++','c') 
answer = [i.upper() for i in programming_languages]
print (answer)

programming_languages_list_upper = []
for i in range (len(programming_languages)):
    programming_languages_list_upper.append(programming_languages[i].upper())
print (programming_languages_list_upper)


#Question 2
'''
Take the following code and rewrite it with a list comprehension.  
 
 # Without using lambdas 
 
def starts_with_A(s): 
      return s[0] == "A" 
 
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"] 
map_object = map(starts_with_A, fruit) 

print(list(map_object)) 
 
This code will result in: 
 
[True, False, False, True, False] 

'''

# def starts_with_A(s): 
#       return s[0] == "A" 

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"] 

for i in fruit:
    if fruit[i][0] == "A":
        return True
    else:
        return False

