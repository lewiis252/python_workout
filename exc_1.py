import numpy as np

def fill_values(height=2, width=3, value=255):
    matrix = [[value]*width for i in range(height)]
    print(matrix)
mat = [
    [1,2,3,3],
    [4,5,6,6],
    [7,8,9,9]
]
def trace(matrix):
    sum = 0
    for i in range(len(matrix)):
        t = matrix[i][i]
        sum = sum + t
    return sum

# print(trace(mat))

def transpose(matrix):
    transposed_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed_matrix.append(new_row)

    return transposed_matrix

# print(transpose(mat))


def top_n(items, n):
    top_values = []

    for i in range(n):
        max_val = max(items)
        top_values.append(max_val)
        items.remove(max_val)

    return top_values

print(top_n([4,5,2,9,5,2,8,2,8,10],3))









