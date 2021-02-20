from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
import time, colorama, os, platform


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


def log_finder(driver_browser):
    log_files = {
        'Chrome': 'chromedriver.log',
        'Edge': 'msedgedriver.log',
        'Firefox': 'geckodriver.log'
    }
    for root, dirs, files in os.walk(os.getcwd()):
        dirs = dirs
        if log_files[driver_browser] in files:
            return os.path.join(root, log_files[driver_browser])
        else:
            if not os.path.exists('logs/'):
                os.makedirs('logs/')
            with open(f'logs/{log_files[driver_browser]}', 'a') as f:
                f.close
                pass


def get_driver_options(browser):
    driver_options = {
        'Chrome': webdriver.ChromeOptions,
        'Edge': EdgeOptions,
        'Firefox': webdriver.FirefoxOptions
    }
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
    colorama.init()
    webdriver_browsers = {
        'Chrome': webdriver.Chrome,
        'Edge': Edge,
        'Firefox': webdriver.Firefox
    }
    return webdriver_browsers[select_browser](
        service_log_path=log_finder(select_browser),
        executable_path=identify_os(select_browser),
        options=options
    )
