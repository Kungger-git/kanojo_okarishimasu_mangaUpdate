#!/usr/local/bin/python3

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import webdriver_conf, colorama, os, platform, time, webbrowser


# Main Function for collecting the texts from the website
def main(driver):
    minutes = [f'{i} minute{plural_s(i)} ago' for i in range(1, 60)]
    hours = [f'{i} hour{plural_s(i)} ago' for i in range(1, 24)]
    days = [f'{i} day{plural_s(i)} ago' for i in range(1, 8)]

    driver.get(
        'https://mangajar.com/manga/kanojo-okarishimasu')
    try:
        article = WebDriverWait(driver, 0).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/article[1]'))
        )
        # Grabbing the Title of the Manga
        pages = []
        for tag in article.find_elements_by_tag_name('h1'):
            title = tag.find_element_by_class_name('post-name')
            print('\n')
            print(colorama.Fore.LIGHTCYAN_EX,
                  title.text, colorama.Style.RESET_ALL)
            fmt = f"Read1_{title.text.replace(', ','_').strip()}_"
            pages.append(fmt)

        # Grabbing the new Released Chapter
        for chapter in article.find_elements_by_xpath('/html/body/div[1]/div/article[1]/div/div[2]/a[2]'):
            new = chapter.find_element_by_xpath(
                '/html/body/div[1]/div/article[2]/ul/li[1]/a')
            uploaded = driver.find_element_by_xpath(
                '/html/body/div[1]/div/article[2]/ul/li[1]/span')
            print('\nNew Chapter:', colorama.Fore.GREEN, new.text.replace('Read', 'Chapter'),
                  colorama.Style.RESET_ALL, 'Uploaded ' + uploaded.text)
            uploaded = uploaded.text

            # If the text meets with the time states,
            # it will open the browser for you to read the new chapter
            if uploaded in minutes or uploaded in hours or uploaded in days:
                for page in pages:
                    new_line = page+new.text.split()[1]
                    webbrowser.open(
                        f'https://w11.mangafreak.net/{new_line}'
                    )
    except WebDriverException as err:
        print(colorama.Fore.RED,
              '[!!] WebDriver Failed To Function!', err, colorama.Style.RESET_ALL)
        main(driver)

    finally:
        driver.quit()

# makes the string plural if uploaded.text is != 1
# example: 1 day ago/2 days ago
def plural_s(v):
    return 's' if abs(v) != 1 else ''


# This function searches for your installed WebDriver
def seek_driver(opsys, brs):
    os.chdir('/')
    cwd = os.getcwd()
    drivers = {'Edge': 'msedgedriver',
               'Chrome': 'chromedriver', 'Firefox': 'geckodriver'}
    # windows
    if opsys == 'Windows':
        for root, dirs, files in os.walk(cwd):
            dirs = dirs
            if drivers[brs] + '.exe' in files:
                return os.path.join(root, drivers[brs] + '.exe')

    # macos and linux
    elif opsys == 'Darwin' or opsys == 'Linux':
        for root, dirs, files in os.walk(cwd):
            if drivers[brs] in files:
                return os.path.join(root, drivers[brs])


# This function identifies your OS and proceeds to the seek_driver() function
def identify_os(brs):
    return seek_driver(platform.system(), brs)


# Just converts the seconds into 00:00:00 format
def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)


if __name__ == '__main__':
    colorama.init()
    brs = ['Chrome', 'Edge', 'Firefox']
    for i in range(len(brs)):
        print(brs[i] + '\n')

    select_browser = str(input('Select Browser: '))
    if select_browser == 'cancel':
        quit()
    try:
        if select_browser in brs:
            options = webdriver_conf.get_driver_options(select_browser)
            webdriver_conf.get_all_options(select_browser, options)
            browser = webdriver_conf.get_driver(select_browser, options)

            start = time.time()
            main(browser)
            end = time.time()
            print(colorama.Fore.YELLOW,
                f'\n[*] Scraping took: {convert(end-start)}', colorama.Style.RESET_ALL)
        else:
            raise ValueError('\n\n[!!] Bruh')
    except WebDriverException as err:
        print(colorama.Fore.RED,
            f'\n\n[!!] No WebDriver Found For: {select_browser}', err, colorama.Style.RESET_ALL)
    print('\n\n')
