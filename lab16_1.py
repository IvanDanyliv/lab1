#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re

html = requests.get("http://www.codeabbey.com/index/user_ranking").content
soup = BeautifulSoup(html, 'html.parser')

table = soup.find_all('tr')

with open('rank.csv', 'w') as f:
    for row in table[2:]:
        result = row.get_text().split()
        result = [_.replace(',', '') for _ in result]
        result = ','.join(result)
        f.write(result + '\n')
