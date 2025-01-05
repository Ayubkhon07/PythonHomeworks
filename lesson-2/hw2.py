#1. Given a side of square. Find its perimeter and area.
a=int(input("Enter a:"))
Perimeter=4*a
Area=pow(a,2)
print("Perimeter = ",Perimeter)
print("Area = ",Area)
#2. Given diameter of circle. Find its length.
d=int(input("Enter d:"))
c=3.14*d
print("Circumference = ",c)
#3. Given two numbers a and b. Find their mean.
a=int(input("Enter a:"))
b=int(input("Enter b:"))
m=(a+b)/2
print("Mean = ",int(m))
#4. Given two numbers a and b. Find their sum, product and square of each number.
a=int(input("Enter a:"))
b=int(input("Enter b:"))
s=a+b
p=a*b
sqa=pow(a,2)
sqb=pow(b,2)
print("Sum = ",s)
print("Product = ",p)
print("Square of",a,"=",sqa)
print("Square of",b,"=",sqb)