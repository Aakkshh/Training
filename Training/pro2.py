def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if prime(num):
            primes.append(num)
        num += 1
    return primes

n = 5
prime_numbers = first_n_primes(n)
print(prime_numbers)
