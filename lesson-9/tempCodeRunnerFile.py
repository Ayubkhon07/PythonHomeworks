def digit_sum(k):
    if k == 0:
        return 0
    else:
        return k % 10 + digit_sum(k // 10)
k = int(input("Enter a number: "))
print(digit_sum(k))
