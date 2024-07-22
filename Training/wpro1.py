def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

num1 = 48
num2 = 18
print(gcd(num1, num2))