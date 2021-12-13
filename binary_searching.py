import math
import random

numbers = [random.randint(-1000,1000) for i in range(1000)]

numbers.sort()
print(numbers)
target = 5

start = 0
end = len(numbers) - 1
flag = False

while start <= end:
    mid = math.floor((start+end)/2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

print(flag)