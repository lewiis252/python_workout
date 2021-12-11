import math


def calculate(n):
    primes_factors = []

    i = 2
    while i <= n:
        if n % i == 0:
            n = n/i
            primes_factors.append(i)
        else:
            i = i +1


    return primes_factors

def calculate_biggest_prime_in_decompositions(n):

    primes = calculate(n)
    sorted_primes = sorted(primes)
    return sorted_primes[-1]

print(calculate_biggest_prime_in_decompositions(13195))