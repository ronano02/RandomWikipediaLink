import requests
import webbrowser
from bs4 import BeautifulSoup

def random_wikipedia_article():
    wikiLink = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    soup = BeautifulSoup(wikiLink.text, 'lxml')
    title = soup.find('title').text
    title = title.split('-')
    title = title[0].strip()
    print(f'The title of the article is "{title}"')
    choice = input('Would you like to read this article? (y/n): ')
    print()
    if choice.lower() in ['y', 'yes', 'Yes', 'NO']:
        webbrowser.open(wikiLink.url, new=0)
    elif choice.lower() in ['n', 'no', 'No', 'NO']:
        pass
    else:
        pass

print('Welcome to your Random Wikipedia Link Program! \n \n')
while True:
    random_wikipedia_article()

