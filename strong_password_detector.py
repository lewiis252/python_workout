# strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase
# characters, and has at least one digit

import re

password = ''' '_6a\8Wkgy5bbLq} '''

passwordRegex = re.compile(r'[A-Z]')

password_groups = passwordRegex.search(password)
print(password_groups)


def password_checker(password):
    if len(password) >= 8 and True:
        print('ok')