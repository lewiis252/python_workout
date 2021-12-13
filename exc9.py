def is_palindrome(n):
    result = False
    n_bin = str(bin(n))[2:]
    if str(n) == str(n)[::-1] and n_bin == n_bin[::-1]:
        result = True

    return result

print(is_palindrome(99))
print(is_palindrome(101))