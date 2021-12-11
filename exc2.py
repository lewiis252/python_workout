

def calculate():
    numbers = []

    multiplies_of_5 = {i for i in range(0, 100, 5)}
    multiplies_of_7 = {i for i in range(0, 100, 7)}

    numbers = set(multiplies_of_5.union(multiplies_of_7))

    result = sum(numbers)
    return result

print(calculate())


