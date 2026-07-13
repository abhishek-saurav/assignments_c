def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter position: "))
print("Fibonacci at position", n, "is", fib(n))

print("Fibonacci sequence up to position", n)
for i in range(n + 1):
    print("fib(" + str(i) + ") =", fib(i))
