import requests
from bs4 import BeautifulSoup
import re

# URL of the website to scrape for proxy addresses
url = 'https://www.socks-proxy.net/'

# Make a request to the website
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the proxy addresses
table = soup.find('table', {'id': 'proxylisttable'})

# Initialize an empty list to store the proxies
proxies = []

# Iterate over each row in the table
for row in table.find_all('tr'):
    # Get the columns in the row
    columns = row.find_all('td')
    # If there are columns in the row
    if len(columns) > 0:
        # Get the IP address and port
        ip_address = columns[0].text
        port = columns[1].text
        #Checking if it's a valid IP address
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_address):
            # Append the proxy to the list in the format 'socks5://IP:port'
            proxies.append(f'socks5://{ip_address}:{port}')
    # Add a delay between requests to avoid overwhelming the server
    time.sleep(1)

# Open a file to save the proxies
with open("proxies.txt", "w") as f:
    for proxy in proxies:
        f.write(proxy + "\n")

print("Proxies saved to proxies.txt")
