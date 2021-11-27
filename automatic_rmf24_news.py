import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import csv
from pprint import pprint
import ssl
import numpy as np

# to avoid ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url='https://www.rmf24.pl/fakty'

page = requests.get(url)

# pprint(page.text)

soup = BeautifulSoup(page.text, 'html.parser')
# pprint(soup)

links = np.array([])
for link in soup.find_all('a'):
    # print(link.get('href'))
    links = np.append(links, link.get('href'))

# links = np.sort(links)
# print(links)

correct_links = np.array([])
for link in links:
    if link.startswith('/raporty/raport') or link.startswith('/fakty/'):
        link =  'https://www.rmf24.pl' + link
        correct_links = np.append(correct_links, link)

correct_links = np.array(list(set(correct_links)))
# print(correct_links[0])
test_page = requests.get(correct_links[0])
# print(test_page.text)

page_content = []
page_links = []
pages = {}
page_soup = BeautifulSoup(test_page.content, 'html.parser')
# pprint(page_soup)

for correct_link in correct_links:
    # print('\n')
    # print(correct_link)
    test_page = requests.get(correct_link)
    page_soup = BeautifulSoup(test_page.content, 'html.parser')
    # page_links.append(correct_link)

    current_content = []
    for content in page_soup.find_all('p'):
        current_content.append(content.get_text())
        # page_content.append(content.get_text())
        # print(content.get_text())
    pages[correct_link] = current_content


# print(len(page_links))
# print(len(page_content))
# print(pages)

for link, content in pages.items():
    print('\n')
    print(link)
    for c in content:
        print(c)






