from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from Kanojo_manga_update_sel import identify_os, convert
import time
import colorama


def get_driver_options(browser):
    driver_options = {
        'Chrome' : webdriver.ChromeOptions,
        'Edge' : EdgeOptions,
        'Firefox' : webdriver.FirefoxOptions}
    return driver_options[browser]()

def get_all_options(browser, options):
    if browser == 'Edge':
        options.use_chromium = True
        options.add_argument('headless')
        options.add_argument('disable-gpu')
    elif browser == 'Chrome' or browser == 'Firefox':
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')


def get_driver(select_browser, options):
    try:
        colorama.init()
        start = time.time()
        if select_browser == 'Chrome':
            return webdriver.Chrome(
                executable_path=identify_os(select_browser), options=options)
        elif select_browser == 'Edge':
            return Edge(
                executable_path=identify_os(select_browser), options=options)
        elif select_browser == 'Firefox':
            return webdriver.Firefox(
                executable_path=identify_os(select_browser), options=options)
    finally:
        end = time.time()
        print(colorama.Fore.YELLOW, '\n[*] Driver Found in: ' +
              convert(end-start), colorama.Style.RESET_ALL)
