# Exercise 1: Print first 10 natural numbers using while loop
a=1
while a<=10:
    print(a)
    a+=1
# Exercise 2: Print the following pattern
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Exercise 3: Calculate sum of all numbers from 1 to a given number
n=int(input())
s=0
for i in range(n+1):
    s+=i
print(s)
# Exercise 4: Print multiplication table of a given number
n=int(input())
for i in range(1,11):
    print(n*i)
# Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i%5==0:
        if i>500:
            break
        if i>150:
            continue       
        print(i)
# Exercise 6: Count the total number of digits in a number
number = int(input("Enter a number: "))
count = 0
while number != 0:
    number //= 10  
    count += 1 
print("The total number of digits is:", count)
# Exercise 7: Print the following pattern
n = 5

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
list2=reversed(list1)
for i in list2:
    print(i)

list1 = [10, 20, 30, 40, 50]
l=len(list1)
for i in range(l-1,-1,-1):
    print(list1[i])
# Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10,0,1):
    print(i)
# Exercise 10: Display a message “Done” after the successful execution of the for loop
for i in range(5):
    print(i)
print("done")
# Exercise 11: Print all prime numbers within a range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers between {start} and {end} are:")
for n in range(start, end + 1):
    if n <= 1:
        continue
        
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
            break

    if is_prime:
        print(n)
# Exercise 12: Display Fibonacci series up to 10 terms
n_terms = 10
n1, n2 = 0, 1
count = 0

print("Fibonacci series up to", n_terms, "terms:")

while count < n_terms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
# Exercise 13: Find the factorial of a given number
num=int(input())
f=1
for i in range(1,num+1):
    f*=i
print(f)
# Exercise 14: Reverse a integer number
a = 765542
reversed_number = 0
while a > 0:
    remainder = a % 10  
    reversed_number = reversed_number * 10 + remainder 
    a = a // 10 
print(reversed_number)
# Exercise 15: Print elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l=len(my_list)
for i in range(1,l,2):
    print(my_list[i])
# Exercise 16: Calculate the cube of all numbers from 1 to a given number
input_number = 6
for i in range(1,input_number+1):
    print(f"Current Number is {i}  and the cube is {i*i*i}")
# Exercise 17: Find the sum of the series up to n terms
n = 5
sum=0
num=2
for i in range(1,n+1):
    sum+=num
    num=num*10+2
print(sum)
# Exercise 18: Print the following pattern
n = 5

for i in range(1, n + 1):
    print('* ' * i)

for i in range(n - 1, 0, -1):
    print('* ' * i)