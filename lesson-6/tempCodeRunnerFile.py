a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Ensure a is less than or equal to b
if a > b:
    a, b = b, a

# Use a list comprehension with range() to find even numbers
even_numbers = [x for x in range(a + (a % 2), b + 1, 2)]

print(even_numbers)