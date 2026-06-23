"""
Prime Number Checker
"""

num = int(input("Enter number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime")
