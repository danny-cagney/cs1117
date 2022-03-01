#Recursion: the definition of a operation in terms of itself.
#Recursive programming: Writing functions that call themselves to solve problems.
# Why recursive programming?
#Many functional languages use recursion only (no loops)i.e. Haskell
#Leads to elegant solutions
#It solve solutions better than iteration
#It can be slower, performance isn't always as efficient as an iterative solution
#Python default is set at 1000 instants of memory.

#Recursion breaks a bigger problem into smaller occurrences of the same problem

# 0 -> Base Case ---- It is a simplest / smallest part of the problem. A simple occurrence that can be answered directly.
# N + 1 -> Recursive case ---- Look at the case behind them and add (+1). A more complex occurrence of the problem that can not
# be answered directly.

"""     // base-case 
        if (issmallEnough(input))
            compute something
            
        else (recursion(input))
        
"""


#Summation (Iterative Version)
def summationI(n):
    sum = 0
    for count in range(1, n+1, 1):
        sum = sum + count
        print (sum)
    return sum

print (summationI(5))



#Summation (Recursive Version)
def summationR(n):
    if n == 0:
        return 0
    else:
        sum = n + summationR(n-1)
        print (sum)
    return sum

print (summationR(5))

def factorialI(n):
    fact = 1
    for count in range (2, n+1, 1):
        fact = fact*count
        print (fact)
    return fact

print(factorialI(5))

def factorialR(n):
    if n == 1:
        return 1
    else:
        return n * factorialR(n-1)

print(factorialR(5))