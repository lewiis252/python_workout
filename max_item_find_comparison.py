import random
import time

l = [random.randint(-10000000, 10000000) for i in range(1048576)]

import pandas as pd


df = pd.DataFrame(l)
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False, header=False)
writer.save()


start = time.time()
def top_n(items, n):
    top_values = []
    items1 = items.copy()
    for i in range(n):
        max_val = max(items1)
        top_values.append(max_val)
        items1.remove(max_val)

    return top_values

# print(top_n([4,5,2,9,5,2,8,2,8,10],3))
print(top_n(l, 10))
stop = time.time()
print('First time {}'.format(stop - start))

start = time.time()

def top_n2(items, n):
    items.sort(reverse=True)
    return items[:n]

print(top_n2(l, 10))

stop = time.time()
print('Second time {}'.format(stop - start))

start = time.time()
def top_n3(items, n):
    items1 = items.copy()
    for i in range(n):
        min_val = min(items1)
        items1.remove(min_val)

    return items1.sort(reverse=True)

# print(top_n([4,5,2,9,5,2,8,2,8,10],3))
print(top_n(l, 10))
stop = time.time()
print('Third time {}'.format(stop - start))