a = [1,2,3,4,5]
b = [2,2,9,0,9]
result = list(zip(a,b))
print (result)

# lambda <input> : <expression>

#Example 1
f = lambda x, y: x + y
print (f(1,1))

#Example 2
lambda pair: max(pair)

#Map takes a function and applies it to each item in an iterable
#map(some_function, some_iterable)

# def fahrenheit(T):
#     return

# def celsius(T):
#     return

# temp = (36.5)

# F = map(fahrenheit, temp)
# C = map(celsius, F)

#List comprehension
#List comprehension is the following structure
#List_comprehension = #[expression iterator conditional]

def chooseLargest(a,b):
    list_len = len(a)
    results = [max(a[i], b[i]) for i in range (list_len)] #list comprehension
    print (results)

    #map (some_function, some_iterable)
    #map (lambda <input> : <expression>, a, b )

    # results = map(lambda num1, num2 : max(num1, num2), a, b)

    # results = list(map(lambda num1, num2 : max(num1, num2), a, b))
    
    # results = list(map(lambda num1, num2 : max(num1, num2), zip(a, b)))

def chooseLargest(a,b):
    results = list(map(lambda pair: max(pair[0], pair[1]), zip(a, b)))
    print (results)

chooseLargest(a,b)