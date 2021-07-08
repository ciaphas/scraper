from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

#locating the box that contains the movie title below

box = soup.find('article', class_='main-article')

#get the h1 tag from the box

title = box.find('h1').get_text()

#get the transcript from the page

transcript = box.find('div', class_='full-script')
transcript = transcript.get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)
