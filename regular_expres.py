import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My numbers is 415-555-4242')
print(mo.group())
print(mo.group(1))