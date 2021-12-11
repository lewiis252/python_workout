
def fibonacci(n):
    f0 = 0
    f1 = 1

    for i in range(n):
        f0, f1 = f1, f1 + f0

    return f0



def calculate():
    total = 0
    i = 0

    while fibonacci(i) < 1000000:
        if i % 2 == 0:
            total = total + fibonacci(i)
        i= i+1

    return total

print(calculate())


