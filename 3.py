# Problem 3 - Largest prime factor

import math

def findprime(num):
    prime = 0
    limit = int(math.sqrt(num) + 1)
    for i in range(2, limit+1):
        if (num % i == 0):
            prime = i
            break
    if (prime == 0):
        prime = num
    return prime


num = 600851475143

while (num != 1):
    prime = findprime(num)
    num /= prime

print prime
