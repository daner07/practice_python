from bs4 import BeautifulSoup
import urllib.request

request = urllib.request.urlopen('https://www.ua-football.com/sport')
html = request.read()

soup = BeautifulSoup(html, 'html.parser')

news = soup.find_all('li', class_='liga-news-item')

result = []

for item in news:
    title = item.find('span', class_='fz-16 fw-500 d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop fz-12').get_text(strip=True)
    href = item.a.get('href')

    result.append({
        'title': title,
        'desc': desc,
        'href': href,
    })


i = 1
f = open('news-test.txt', 'w', encoding='utf-8')
for item in result:
    f.write(
        f'Новость № {i} \n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: https://www.ua-football.com/sport{item["href"]}\n\n *********\n\n')
    i += 1
f.close()
