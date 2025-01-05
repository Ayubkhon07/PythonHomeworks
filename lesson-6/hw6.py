#1. Find leap year.
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap = True
else:
    is_leap = False

print(is_leap)  # Output: True
#2. Task Given an integer, , perform the following conditional actions: If is odd, print Weird If is even and in the inclusive range of to , print Not Weird If is even and in the inclusive range of to , print Weird If is even and greater than , print Not Weird Input Format A single line containing a positive integer, . Constraints Output Format Print Weird if the number is weird. Otherwise, print Not Weird.
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

n = int(input())
check_weird(n)
#3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop. 
#if-else
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a % 2 != 0:
    a += 1
if b % 2 != 0:
    b -= 1

if a <= b:
    even_numbers = list(range(a, b + 1, 2))
else:
    even_numbers = []

print(even_numbers)

#without
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

even_numbers = list(range(a + a % 2, b - b % 2 + 1, 2))

print(even_numbers)