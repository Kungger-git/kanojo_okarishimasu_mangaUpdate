from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import colorama, time


def main(driver):
    driver.get(
        'https://mangajar.com/manga/kanojo-okarishimasu')
    try:
        getTitle = WebDriverWait(driver, 0).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/article[1]/div/h1/span[1]'))
        )
    finally:
        pass
    time.sleep(1)
    driver.quit()

    print(getTitle)
    

if __name__ == '__main__':
    edge = webdriver.Edge(
        '/Users/jimfe/Documents/msedgedriver.exe')
    colorama.init()
    main(edge)