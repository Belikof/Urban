import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if math.sqrt(i).is_integer() == False:
        primes.append(i)
    else:
        not_primes.append(i)

print("Prime numbers:", primes)
print("Not prime numbers:", not_primes)