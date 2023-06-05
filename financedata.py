import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define the URL of the webpage containing the tables
url = 'https://finviz.com/quote.ashx?t=STOCKSYMBOLHERE&p=d'

# Send an HTTP GET request with custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the specific tables on the webpage
    tables = []
    tables_to_extract = [10, 12, 14, 15]

    for i in tables_to_extract:
        table = soup.find_all('table')[i - 1]
        tables.append(table)

    # Extract the data from each table and save to CSV files
    for i, table in enumerate(tables):
        rows = table.find_all('tr')
        data = []
        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_data = [cell.get_text(strip=True) for cell in cells]
            data.append(row_data)

        df = pd.DataFrame(data)
        df.to_csv(f'table_{tables_to_extract[i]}.csv', index=False, header=False)
        print(f"Table {tables_to_extract[i]} saved as table_{tables_to_extract[i]}.csv")
else:
    print('Failed to retrieve the webpage:', response.status_code)
