# Homework2:

# Given two integer variables: a and b. Swap the values of the variables.
a = int(input())
b = int(input())

# write code here. Don't change given conditions

print(a, b)

#1
a = int(input())
b = int(input())

c = a
a = b
b = c

print(a, b)

#2
a = int(input())
b = int(input())

a, b = b, a

print(a, b)
