numbers = [-11, 2, -3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if -10 < i < 10:
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)