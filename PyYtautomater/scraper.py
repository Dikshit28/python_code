import json
import combiner
import download
from datetime import date
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
#option.add_argument('--headless')
#option.add_argument('--disable-gpu')
# option.add_argument("--incognito") OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
def login():
    browser.get("https://www.instagram.com/")
    username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear()
    username.send_keys("_reels_downloader_")
    password.clear()
    password.send_keys("reelsdownloader")
    loginbutton = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    notnow = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    notnow2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

def audio_page():
    browser.get("https://www.instagram.com/reels/audio/476281126767191/")
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="Tjpra"]/a[@tabindex="0"]')))
    a_tags=browser.find_elements_by_xpath('//div[@class="Tjpra"]/a[@tabindex="0"]')
    print(len(a_tags))
    links=[link.get_attribute('href') for link in a_tags]
    return links

def download(links):
    usernames=[]
    video_urls=[]
    for link in links:
        browser.get(link+"?__a=1")
        element=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/pre')))
        data=browser.find_element_by_xpath('/html/body/pre').text
        json_data=json.loads(data)
        video_url=json_data['graphql']['shortcode_media']['video_url']
        username=json_data['graphql']['shortcode_media']['owner']['username']
        usernames.append(username)
        video_urls.append(video_url)
    return video_urls,usernames

#Run this every day at 12:00 AM
login()
links=audio_page()
video_urls,usernames=download(links)
download.downloader(video_urls,usernames)
combiner.combine("./reels-"+str(date.today())+"/",usernames,(date.today()))
#Add deleter.py after uploading to youtube
browser.quit()

