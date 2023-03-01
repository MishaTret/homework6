import lxml
from bs4 import BeautifulSoup
import requests

url = 'https://kups.club/'
agent = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

params = {'admin': '123'}

response = requests.get(url, headers=agent)
print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")
# print(soup)

all_product = soup.find('ul', class_='row mt-4')
print(all_product)
list_product = all_product.find_all('li', class_='card h-100')
print(list_product[0].text)

for elem in list_product:
    title = elem.find('span', class_='card-title')
#    print(title.text)
with open('product.txt', 'a', encoding='UTF8') as f:
    for elem in list_product:
        title = elem.find('span', class_='card-title')
        product_name = title.text.strip()
        print(product_name)
        f.write(f'{product_name}\n')
