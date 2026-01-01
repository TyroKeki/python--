import math
"""O(nloglogn)"""
n = int(input())
primes = []
is_prime = [True] * (n + 1) #MX为最大可能遇到的质数加1
is_prime[1] = is_prime[0] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

for i in range(2,n+1):
    if is_prime[i]: primes.append(i)

print(primes)