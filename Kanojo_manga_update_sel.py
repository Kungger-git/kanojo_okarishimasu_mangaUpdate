from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import colorama, os


def main(driver):
    driver.get(
        'https://mangajar.com/manga/kanojo-okarishimasu')

    try:
        article = WebDriverWait(driver, 0).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/article[1]'))
        )
        for tag in article.find_elements_by_tag_name('h1'):
            title = tag.find_element_by_class_name('post-name')
            print('\n')
            print(colorama.Fore.LIGHTCYAN_EX, title.text, colorama.Style.RESET_ALL)

        for chapter in article.find_elements_by_xpath('/html/body/div[1]/div/article[1]/div/div[2]/a[2]'):
            new = chapter.find_element_by_class_name('h-6')
            time = driver.find_element_by_xpath('/html/body/div[1]/div/article[2]/ul/li[1]/span')
            print('\nNew Chapter:')
            print(colorama.Fore.GREEN, new.text.replace('Read', 'Chapter'), colorama.Style.RESET_ALL, time.text)
    finally:
        driver.quit()

def look_for_driver():
    os.chdir('/')
    cwd = os.getcwd()
    for root, dirs, files in os.walk(cwd):
        if 'msedgedriver.exe' in files:
            return os.path.join(root, 'msedgedriver.exe')
        elif 'msedgedriver' in files:
            return os.path.join(root, 'msedgedriver')

if __name__ == '__main__':
    edge = webdriver.Edge(look_for_driver())
    colorama.init()
    main(edge)
    print('\n\n')