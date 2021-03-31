from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

payload = {
    'tbUserName': '19CSU379',
    'tbPassword': 'dikshit_12345'
}
driver_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, options=option)
browser.get("http://erp.ncuindia.edu/Welcome_iie.aspx")
username = browser.find_element_by_id("tbUserName")
username.send_keys("19CSU379")
pas = browser.find_element_by_id("tbPassword")
pas.send_keys("dikshit_12345")
pas.send_keys(Keys.RETURN)
data = ""
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "aAttandance"))
    )
    aten = browser.find_element_by_id("aAttandance").get_attribute("href")
    browser.get(aten)
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='aspnetForm']/div[3]/div/div/div[2]/div/div/section/div/div[2]/table/tbody/tr"))
        )
        tr = len(browser.find_elements_by_xpath(
            "//*[@id='aspnetForm']/div[3]/div/div/div[2]/div/div/section/div/div[2]/table/tbody/tr"))
        tc = len(browser.find_elements_by_xpath(
            "//*[@id='aspnetForm']/div[3]/div/div/div[2]/div/div/section/div/div[2]/table/tbody/tr[1]/td"))

        before_XPath = "//*[@id='aspnetForm']/div[3]/div/div/div[2]/div/div/section/div/div[2]/table/tbody/tr["
        aftertd_XPath = "]/td"
        for t_tr in range(0, tr):
            FinalXPath = before_XPath + str(t_tr) + aftertd_XPath
            cell_text = browser.find_elements_by_xpath(FinalXPath)
            data = data+cell_text[1].text+"--"+cell_text[6].text+"\n\n"
    except:
        pass
except:
    pass
print(data)
browser.quit()
