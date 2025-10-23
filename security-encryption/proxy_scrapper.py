import requests
from bs4 import BeautifulSoup

url = "https://free-proxy-list.net"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
table = soup.find('table', class_="table")

for row in table.find_all('tr'):
    columns = row.find_all('td')

    if columns != []:
        ip = columns[0].text.strip()
        port = columns[1].text.strip()
        code = columns[2].text.strip()
        anonymity = columns[3].text.strip()
        last_checked = columns[-1].text.strip()

        with open("security-encryption/proxies.txt", "a") as f:
            f.write(f"{id} - {port} - {code} - {anonymity} - {last_checked}\n")
