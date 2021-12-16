import pandas as pd
from urllib.parse import urlparse
import numpy as np

# load data
df = pd.read_excel('Web_scraping.xlsx', sheet_name='Slawek')
# make domains
domains = [urlparse(domain).netloc for domain in np.array(df['url'])]
df['domain'] = domains

#save changes
df.to_excel('test.xlsx')

# create tuples
tuples = [tuple(r) for r in df.to_numpy()]
print(tuples)


