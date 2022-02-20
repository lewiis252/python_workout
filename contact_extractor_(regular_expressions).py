import re

'''phone number extractor part'''

phoneRegex = re.compile(r'''(
(\+\d{2}|\+\(\d{2}\))? #numer kierunkowy
(\s|-|)? # separator 
(\d{3}) # three digits
(\s|-|) # separator
(\d{3}) # three digits
(\s|-|) # separator
(\d{3}) # three digits 
)''', re.VERBOSE)

text_to_search = 'Sed ut perspiciatis, 111111111 unde omnis 111-111-111 iste natus 111 111 111 error (+48) 111 111 111 sit voluptatem +48 111-111-111'

numbers_found = phoneRegex.findall(text_to_search)
for group in numbers_found:
    joined = '-'.join([group[3], group[5], group[7]])
    print(joined)
print(numbers_found)

'''email extractor part'''

emailRegex = re.compile(r'''(
[a-zA-Z0-9.%+-]+ #username
@
[a-zA-Z0-9.%+-]+ # domain name
\.[a-zA-Z]{2,4} # dot something
)''', re.VERBOSE)

text_to_search = 'Sed ut perspiciatis, lewifasfasfais252@gmail.com unde omnis lewsdasdafiis@gmail.com iste natus 111 111 111  error (+48) 111 111 111 sit voluptatem +48 111-111-111'

email_found = emailRegex.findall(text_to_search)
print(email_found)
for group in email_found:
    print(group)
