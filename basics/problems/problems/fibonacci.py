"""
Fibonacci Series
"""

n = int(input("Enter terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a+b
