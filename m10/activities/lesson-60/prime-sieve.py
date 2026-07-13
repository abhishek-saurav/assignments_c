n = int(input("Find all primes up to: "))

is_prime = []
for i in range(n + 1):
    is_prime.append(True)

is_prime[0] = False
if n >= 1:
    is_prime[1] = False

p = 2
while p * p <= n:
    if is_prime[p]:
        multiple = p * p
        while multiple <= n:
            is_prime[multiple] = False
            multiple = multiple + p
    p = p + 1

primes = []
for i in range(n + 1):
    if is_prime[i]:
        primes.append(i)

print("Primes up to", n, ":", primes)
print("Total count:", len(primes))
