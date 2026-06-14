def fibonacci(n):
    first = 0
    second = 1
    print("Fibonacci series:")
    for i in range(n):
        print(first, end=' ')
        temp = first + second
        first = second
        second = temp

n = int(input("Enter the number of terms: "))
fibonacci(n)
