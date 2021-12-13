def greatest_common_divisor(a,b):
    result = 1
    for i in range(1, max(a,b)):
        if a % i == 0 and b % i == 0:
            result =i

    return result

print(greatest_common_divisor(32,48))