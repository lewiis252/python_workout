# this program extracts date dd/mm/yyy from text, date may be not real!!!

import re

dateRegex = re.compile(r'''(
(\d?\d)
(/|-|.)
(\d?\d)
(/|-|.)
(\d{4})
)''', re.VERBOSE)

text = ' kot 21.01.2022 and 21-01-2022 and 1/12/2022'

date_found = dateRegex.findall(text)
print(date_found)

# format it a bit better
for group in date_found:
    formatted_date = '.'.join([group[1], group[3], group[5]])
    print(formatted_date)
