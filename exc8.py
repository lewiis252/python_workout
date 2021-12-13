def is_prime(n):
    result = True

    for i in range(2,int(n/2)+1):
        if n % i == 0:
            result = False
            break
    if n == 1:
        result = False
    return result

def nth_prime(n):
    counter = 0
    i = 2
    while counter != n:
        if is_prime(i):
            counter = counter + 1
        i = i+1
    return i-1, counter

