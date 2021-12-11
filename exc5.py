def three_digits_palindromes():

    numbers = [number for number in range(100, 1000) if str(number)[::-1] == str(number)]
    return len(numbers)

print(three_digits_palindromes())


