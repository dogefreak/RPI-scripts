from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.request import urlopen

options = Options()
options.add_argument("user-data-dir=/home/pi/.config/chromium/") # change to profile path
options.add_argument("profile-directory=Default")
driver = webdriver.Chrome(options=options)

def internet():
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
    except: 
        return False

def deezer():
    driver.get("http://deezer.com/us/flow")

    flowButton = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Play"]')))

    time.sleep(1)
    flowButton.click()    

if internet: deezer()
else: exit()
