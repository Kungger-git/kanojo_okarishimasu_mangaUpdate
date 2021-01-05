from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import colorama
import os
import platform
import time
import webbrowser


# Main Function for collecting the texts from the website
def main(driver):
    time_states = ['Today', '1 day ago', '2 days ago',
                   '3 days ago', '4 days ago', '5 days ago', '6 days ago']
    driver.get(
        'https://mangajar.com/manga/kanojo-okarishimasu')
    try:
        article = WebDriverWait(driver, 0).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/article[1]'))
        )
        # Grabbing the Title of the Manga
        for tag in article.find_elements_by_tag_name('h1'):
            title = tag.find_element_by_class_name('post-name')
            print('\n')
            print(colorama.Fore.LIGHTCYAN_EX,
                  title.text, colorama.Style.RESET_ALL)

        # Grabbing the new Released Chapter
        for chapter in article.find_elements_by_xpath('/html/body/div[1]/div/article[1]/div/div[2]/a[2]'):
            new = chapter.find_element_by_class_name('h-6')
            time = driver.find_element_by_xpath(
                '/html/body/div[1]/div/article[2]/ul/li[1]/span')
            print('\nNew Chapter:')
            print(colorama.Fore.GREEN, new.text.replace('Read', 'Chapter'),
                  colorama.Style.RESET_ALL, 'Uploaded ' + time.text)

            # If the text meets with the time states,
            # it will open the browser for you to read the new chapter
            if time.text in time_states:
                webbrowser.open(
                    'https://w11.mangafreak.net/Manga/Kanojo_Okarishimasu?')
    except WebDriverException as err:
        print(colorama.Fore.RED,
              '[!!] WebDriver Failed To Function!', err, colorama.Style.RESET_ALL)
    finally:
        driver.quit()

# This function searches for your installed WebDriver
def seek_driver(opsys, brs):
    os.chdir('/')
    cwd = os.getcwd()
    drivers = ['msedgedriver', 'chromedriver', 'geckodriver']
    # windows
    if opsys == 'Windows':
        for root, dirs, files in os.walk(cwd):
            if drivers[0] + '.exe' in files and brs == 'Edge':
                return os.path.join(root, 'msedgedriver.exe')
            elif drivers[1] + '.exe' in files and brs == 'Chrome':
                return os.path.join(root, 'chromedriver.exe')
            elif drivers[2] + '.exe' in files and brs == 'Firefox':
                return os.path.join(root, 'geckodriver.exe')

    # macos
    elif opsys == 'Darwin':
        for root, dirs, files in os.walk(cwd):
            if drivers[0] in files and brs == 'Edge':
                return os.path.join(root, 'msedgedriver')
            elif drivers[1] in files and brs == 'Chrome':
                return os.path.join(root, 'chromedriver')
            elif drivers[2] in files and brs == 'Firefox':
                return os.path.join(root, 'geckodriver')

    # linux
    elif opsys == 'Linux':
        for root, dirs, files in os.walk(cwd):
            if drivers[0] in files and brs == 'Edge':
                return os.path.join(root, 'msedgedriver')
            elif drivers[1] in files and brs == 'Chrome':
                return os.path.join(root, 'chromedriver')
            elif drivers[2] in files and brs == 'Firefox':
                return os.path.join(root, 'geckodriver')

# This function identifies your OS and proceeds to the seek_driver() function
def identify_os(brs):
    operating_system = platform.system()
    return seek_driver(operating_system, brs)

# Just converts the seconds into 00:00:00 format
def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)


if __name__ == '__main__':
    colorama.init()
    brs = ['Chrome', 'Edge', 'Firefox']
    for br in brs:
        print(br + '\n')

    select_browser = str(input('Select Browser: '))
    if select_browser == 'cancel':
        quit()
    try:
        start = time.time()
        # For Chrome
        if select_browser in brs and select_browser == 'Chrome':
            browser = webdriver.Chrome(
                executable_path=identify_os(select_browser))
            end = time.time()
            print('\nTime Elapsed: ' + str(convert(end-start)))
            main(browser)
        # For Edge
        elif select_browser in brs and select_browser == 'Edge':
            browser = webdriver.Edge(
                executable_path=identify_os(select_browser))
            end = time.time()
            print('\nTime Elapsed: ' + str(convert(end-start)))
            main(browser)
        # For Firefox
        elif select_browser in brs and select_browser == 'Firefox':
            browser = webdriver.Firefox(
                executable_path=identify_os(select_browser))
            end = time.time()
            print('\nTime Elapsed: ' + str(convert(end-start)))
            main(browser)
    except WebDriverException as err:
        print(colorama.Fore.RED, '\n\n[!!] No WebDriver Found For ' +
              select_browser, err, colorama.Style.RESET_ALL)
    print('\n\n')
