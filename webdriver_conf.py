from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from Kanojo_manga_update_sel import identify_os


def get_driver_options(browser):
    if browser == 'Chrome':
        return webdriver.ChromeOptions()
    elif browser == 'Edge':
        return EdgeOptions()
    elif browser == 'Firefox':
        return webdriver.FirefoxOptions()


def get_all_options(browser, options):
    if browser == 'Edge':
        options.use_chromium = True
        options.add_argument('headless')
        options.add_argument('disable-gpu')
    elif browser == 'Chrome' or 'Firefox':
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')


def get_driver(select_browser, options):
    if select_browser == 'Chrome':
        return webdriver.Chrome(
            executable_path=identify_os(select_browser), options=options)
    elif select_browser == 'Edge':
        return Edge(
            executable_path=identify_os(select_browser), options=options)
    elif select_browser == 'Firefox':
        return webdriver.Firefox(
            executable_path=identify_os(select_browser), options=options)
    else:
        raise KeyError(select_browser + ' does not exist')
