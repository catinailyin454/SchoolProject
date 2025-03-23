import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find('table').find_all('tr')

df = pd.DataFrame(columns=['Name', 'Age', 'Country'])

for row in data:
    cols = [col.get_text() for col in row.find_all('td')]
    df.loc[len(df)] = cols

print(df)
