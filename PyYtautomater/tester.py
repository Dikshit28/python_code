import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
warnings.filterwarnings('ignore')
driver_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
link="https://www.instagram.com/reel/CPsYTv1lSLy/"
browser.get(link)
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@tabindex="0"]')))

a_tags=browser.find_elements_by_xpath('//a[@tabindex="0"]')
print(a_tags[0])
