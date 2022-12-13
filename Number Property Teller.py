x = int(input())

# Even or Odd!

def EveOdd(x):
    if x % 2 == 0:
        print(x,"is an Odd Number.")
    else:
        print(x,"is an Odd Number.")

# Sum of Natural Numbers till x

def sumn(x):
    sum1 = 0
    for i in range(x + 1):
        sum1 += i
    print("Sum of Natural numbers till",x,"is :",sum1)

# Factors of x!

def factrs(x):
    print("The factors of", x, "are :")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end=",")


# Palindrome or not?!

def palindrome(x):
    x = str(x)
    if x == x[::-1]:
        print("Yes!", x, "is a palindrome.")
    else:
        print("No!", x, "isn't a palindrome.")

# Prime or Composite number

def prime(x):
    list2 = []
    for i in range(1, x + 1):
        list2.append(i)
    if len(list2) <= 2:
        print(x,"is a Prime number.")
    else:
        print(x,"is a Composite number.")



# Fibonacci Series

def fn(x):

    nterms = x

    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")

    elif nterms == 1:
        print("Fibonacci sequence till", nterms, "are :")
        print(n1, end="")
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence till",x,"terms are :")
        while count < nterms:
            print(n1, end=", ")
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

def factorial(x):
    factorial1 = 1
    if x == 0:
        print("1")
    elif x == 1:
        print(1)
    else:
        for i in range(1, x + 1):
            factorial1 = factorial1 * i
        print("The value of", x, "factorial is :", factorial1)

EveOdd(x)
sumn(x)
factrs(x)
print( )
prime(x)
palindrome(x)
fn(x)
print( )
factorial(x)