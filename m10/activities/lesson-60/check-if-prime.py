n = int(input("Enter a number: "))

if n < 2:
    print(n, "is not a prime number")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i = i + 1

    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
