import math

def is_prime(n):
    result = True

    for i in range(2,int(n/2)+1):
        if n % i == 0:
            result = False
            break
    if n == 1:
        result = False
    return result

for i in range(1, 101):
    print(f'is {i} prime?: {is_prime(i)}')
