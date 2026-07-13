two_digit_primes = []

n = 10
while n <= 99:
    if n >= 2:
        is_prime = True
        i = 2
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i = i + 1
        if is_prime:
            two_digit_primes.append(n)
    n = n + 1

print("All 2-digit prime numbers:")
print(two_digit_primes)
print("Total count:", len(two_digit_primes))
