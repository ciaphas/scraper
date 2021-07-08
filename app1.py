from bs4 import BeautifulSoup
import requests

website = 'https://www.bbc.co.uk/news'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())


with open('website.txt', 'w') as file:
    file.write(soup.prettify())

box = soup.find_all('a', href=True)
box1 = soup.find('div')


with open('bbclinks.txt', 'w') as file1:
    for link in soup.find_all('a', href=True):
        print (link.get('href'))
