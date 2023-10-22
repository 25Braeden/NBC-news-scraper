import requests
from bs4 import BeautifulSoup

url = input("Enter the URL of the NBC News story you want to scrape: ")

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    story_elements = soup.find_all('div', class_='article-body__content')
    with open('nbc_news_story.txt', 'w', encoding='utf-8') as file:
        for element in story_elements:
            story_text = element.get_text()
            file.write(story_text)
    print("Scraped content saved to 'nbc_news_story.txt'.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
