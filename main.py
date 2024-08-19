from bs4 import BeautifulSoup
import requests

url = 'https://www.avito.ru/moskva_i_mo/avtomobili/mercedes-benz-ASgBAgICAUTgtg3omCg?cd=1&p='

results = []

for i in range(1, 3):
    print(i)
    page = requests.get(f'{url}{i}')
    soup = BeautifulSoup(page.content, "html.parser")
    allItems = soup.findAll('div', attrs={'data-marker': 'item'})

    for item in allItems:
        name = item.find(attrs={'itemprop': 'name'}).text
        price = item.find(attrs={'itemprop': 'price'}).attrs['content']
        item_obj = {
            'name': name,
            'price': price
        }
        results.append(item_obj)

file = open("data.json", "w")
file.write(f'{results}')
file.close()

print(results)
