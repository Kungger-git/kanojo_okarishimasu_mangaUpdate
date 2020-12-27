from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import colorama
import os
import platform
import time


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
            print(colorama.Fore.LIGHTCYAN_EX,
                  title.text, colorama.Style.RESET_ALL)

        for chapter in article.find_elements_by_xpath('/html/body/div[1]/div/article[1]/div/div[2]/a[2]'):
            new = chapter.find_element_by_class_name('h-6')
            time = driver.find_element_by_xpath(
                '/html/body/div[1]/div/article[2]/ul/li[1]/span')
            print('\nNew Chapter:')
            print(colorama.Fore.GREEN, new.text.replace('Read', 'Chapter'),
                  colorama.Style.RESET_ALL, 'Uploaded ' + time.text)
    finally:
        driver.quit()


def seek_driver(opsys):
    os.chdir('/')
    cwd = os.getcwd()
    if opsys == 'Windows':
        for root, dirs, files in os.walk(cwd):
            if 'msedgedriver.exe' in files:
                return os.path.join(root, 'msedgedriver.exe')
            elif 'chromedriver.exe' in files:
                return os.path.join(root, 'chromedriver.exe')

    elif opsys == 'Darwin':
        for root, dirs, files in os.walk(cwd):
            if 'msedgedriver' in files:
                return os.path.join(root, 'msedgedriver')
            elif 'chromedriver' in files:
                return os.path.join(root, 'chromedriver')


def identify_os():
    operating_system = platform.system()
    return seek_driver(operating_system)


def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)


if __name__ == '__main__':
    colorama.init()
    brs = ['Chrome', 'Edge']
    for br in brs:
        print(br + '\n')

    select_browser = str(input('Select Browser: '))
    if select_browser == 'cancel':
        quit()
    try:
        start = time.time()
        if select_browser == 'Chrome':
            browser = webdriver.Chrome(identify_os())
            end = time.time()
            print('\nTime Elapsed: ' + str(convert(end-start)))
            main(browser)
        elif select_browser == 'Edge':
            browser = webdriver.Edge(identify_os())
            end = time.time()
            print('\nTime Elapsed: ' + str(convert(end-start)))
            main(browser)
    except WebDriverException as err:
        print('\n\nNo WebDriver Found For ' + select_browser, err)
    print('\n\n')
