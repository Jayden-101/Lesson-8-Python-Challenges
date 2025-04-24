a = int(input("Enter First Number (a):"))
b = int(input("Enter Second Number (b):"))
c = int(input("Enter Third Number (c):"))

print(f"\nBefore swapping:\n a = {a}, b ={b}, c = {c}")

temp = a
a = b
b = c
c = temp
print(f"\nAfter swapping:\n a {a}, b = {b}, c = {c}")
