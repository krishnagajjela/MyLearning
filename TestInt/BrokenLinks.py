import requests
from selenium import webdriver
from webdrivermanager import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

ActionChains.key_down(Keys.SHIFT).send_keys("abc").key_down(Keys.SHIFT)

gdd = GeckoDriverManager()
gdd.download_and_install()
driver =webdriver.Firefox()
driver.get("http://apress.com/")
images=driver.find_elements_by_css_selector("a") #link --> href and img --> src
for image in images:
    if (requests.head(image.get_attribute('href')).status_code==200):
        print("Valid Image Link.")
    else:
        print("Invalid Image Link.")