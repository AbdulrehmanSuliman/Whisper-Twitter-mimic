from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import accessabilities


def driver_setup():
    # initializing webdriver
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    s = Service(accessabilities.chrome_driver)
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=s, options=chrome_options, desired_capabilities=caps)
    driver.implicitly_wait(20)
    driver.maximize_window()
    return driver


driver = driver_setup()
