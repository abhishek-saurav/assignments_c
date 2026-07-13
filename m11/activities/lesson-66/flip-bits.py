n = int(input("Enter a number: "))
k = int(input("How many bits to flip from the right? "))

mask = (1 << k) - 1
result = n ^ mask

print("Original number:", n, "->", bin(n))
print("After flipping rightmost", k, "bits:", result, "->", bin(result))
