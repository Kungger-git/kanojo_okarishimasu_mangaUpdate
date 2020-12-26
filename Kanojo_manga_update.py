import requests, colorama
from bs4 import BeautifulSoup as soup

def main():
    try:
        req = requests.get(
            'https://mangajar.com/manga/kanojo-okarishimasu', timeout=1)
        req.raise_for_status()
        page_soup = soup(req.text, 'html.parser')

        getInfo(page_soup)
    except requests.exceptions.RequestException as err:
        print('Request Failed! ', err)

def getInfo(loc):
    print(colorama.Fore.LIGHTCYAN_EX, '\nKanojo Okarishimasu\n', colorama.Style.RESET_ALL)
    for container in loc.findAll('h2', {'class':'h-6'})[1]:
        print('New Chapter:', colorama.Fore.LIGHTGREEN_EX, container, colorama.Style.RESET_ALL)

if __name__ == '__main__':
    colorama.init()
    main()
    print('\n\n')
