import random

small = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%&*"
pool = small + caps + digits + symbols

length = 12
password = ""
for i in range(length):
    password = password + random.choice(pool)

print("Your random password is:", password)
