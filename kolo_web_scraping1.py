from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://drogi.gddkia.gov.pl/informacje-drogowe/lista-utrudnien'
strona = urlopen(url, context=ctx)
html = strona.read().decode('utf-8')

parsed = BeautifulSoup(html, 'html.parser')


tab = parsed.find_all('tr')

# pprint(tab)

wynik = []
for row in tab:
    lokalizacja = row.select_one('td.td3')
    if lokalizacja is not None:
        if lokalizacja.text == 'podkarpackie':
            wynik.append(row)
        # pprint(lokalizacja.text)

print(wynik)
