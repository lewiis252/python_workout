import math

numbers = [1,2,3,4,5,6,7,8,9]
numbers.sort()

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