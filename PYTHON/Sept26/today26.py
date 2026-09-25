# You need to perform three separate tasks based on the given input:

# String Input and Print: Read a string s (which may contain spaces) and print it as it is.
# Integer Input and Print: Read an integer n and print it without any change.
# Float Input and floor Print: Read a floating-point number as input, take its floor value, and print as an integer.

import math

# s to store string
# n to store integer
# f to store float
# ff  # To Store floor of float variable f

# code here
s=input()
n=int(input())
ff=float(input())
print(s)
print(n)
print(math.floor(ff))


# Given a number x, print the numbers from x to 0 in decreasing order in a single line.

x = int(input())

# code here
for i in range (x,-1,-1):
    print(i,end=" ")


# Given two integers, n and m. The task is to check the relation between n and m. Print "less" if n < m,  "equal" if n == m, and "greater" if n > m.

n = int(input())
m = int(input())

# code here
if n<m:
    print("less")
elif n==m:
    print("equal")
else:
    print("greater")


# Given a number n, use the if statement to print "Big" (without quotes) if the given number is greater than 100. The statement "Number" (without quotes) will be printed regardless.

# Note: Follow Sample cases for the output format. After printing move the cursor to the next line.

n = int(input())

if n > 100:
    print("Big")

print("Number")


# Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a.
a = int(input())
b = int(input())

# code here
temp=a
temp=b

print(b,a)

# Given two integer variables x and y, perform the following operations:

# p: Addition of x and y
# q: Subtraction of y from x
# r: Multiplication of x and y
# s: Floating-point division of x by y
# t: Integer division of x by y
# u: Modulo (remainder when x is divided by y)

x = int(input())
y = int(input())

# code here
p=x+y
q=x-y
r=x*y
s=x/y
t=x//y
u=x%y

print(p, q, r, f"{s:.3f}", t, u)

# Given a number n, use a switch statement to return "One" if the given number is equal to 1, "Two" if the number is 2 and so on till 9 ("Nine") else return "Unknown"(without quotes). 

n = int(input())

# code here
match n:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("Seven")
    case 8:
        print("Eight")
    case 9:
        print("Nine")
    case _:
        print("Unknown")

# Given an integer n. Write a program to print the last digit of n.

n = input()

# code here
print(n[len(n)-1])

# Given three positive integers a, b and c. Perform some bitwise operations on them as given below:
# 1. d = a ^ a
# 2. e = c ^ b
# 3. f = a & b
# 4. g = ~ e
# Note: ^ is for xor.
# Then print d e f g space seperately. Move the cursor to the next line after printing.

a = int(input())
b = int(input())
c = int(input())

# code here
d=a^a
e=c^b
f=a&b
g=~e
print(d, e, f,g)

