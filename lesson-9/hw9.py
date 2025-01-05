#1 is_prime(n) funksiyasini hosil qiling(n>0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print("True")
else:
    print("False")
#2. k sonining raqamlari yig'indisini hisoblovchi digit_sum(k) rekursiv funksiya tuzing.
def digit_sum(k):
    if k == 0:
        return 0
    else:
        return k % 10 + digit_sum(k // 10)
k = int(input("Enter a number: "))
print(digit_sum(k))
#3. It is required to print all integer powers of two (that is, numbers of the form 2**k) that do not exceed the number N.
n=int(input())
k=0
p=2**k
while p<=n:
    print(p)
    k+=1
    p=2**k