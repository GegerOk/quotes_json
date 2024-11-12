import json
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)  # Получаем запрос

if response.status_code == 200:  # Необходимо для проверки запроса
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все цитаты на странице
    quotes = soup.find_all('div', class_='quote')

    data = []
    for i in quotes:  # Извлекаем текст цитаты, автора и теги
        text = i.find('span', class_='text').getText()
        author = i.find('small', class_='author').getText()
        tags = [tag.getText() for tag in i.find_all('a', class_='tag')]

        data.append({  # Добавляем информацию в словарь
            'text': text,
            'author': author,
            'tags': tags
        })
else:
    print(
        f"Ошибка при получении данных. Код состояния: {response.status_code}")


with open('result.json', 'w', encoding='utf-8') as jsonfile:  # Сохраняем данные в файл JSON
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)
