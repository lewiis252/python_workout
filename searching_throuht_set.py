import math
numbers = [1,2,3,4,5,6,7,8,9]
numbers.sort()

target = 9

start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = math.ceil((start+end)/2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = start + 1
        else:
            end = end - 1

print(flag)