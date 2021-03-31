from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
driver_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# Command Handlers. Usually take two arguments: bot and update.


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Welcome to Attendance bot!!\nSend \n'/username + username'\n'/password + password'\nto store Id and password for future use\n/attendance to get attendance")


def username(update, context):
    payload["uname"] = (context.args)
    context.bot.send_message(
        chat_id=update.message.chat_id, text="Username saved")


def password(update, context):
    payload["pword"] = (context.args)
    context.bot.send_message(
        chat_id=update.message.chat_id, text="Password saved")


def attendance(update, context):

    if payload['uname'] == "" or payload['pword'] == "":
        context.bot.send_message(
            chat_id=update.message.chat_id, text="Username or Password not found\nSend \n'/username + username'\n'/password + password' to store Id and password for future use")
    else:
        context.bot.send_message(
            chat_id=update.message.chat_id, text="Please wait while I check your attendance")
        # Create new Instance of Chrome
        browser = webdriver.Chrome(executable_path=driver_path, options=option)
        browser.get("http://erp.ncuindia.edu/Welcome_iie.aspx")
        username = browser.find_element_by_id("tbUserName")
        username.send_keys(payload['uname'])
        pas = browser.find_element_by_id("tbPassword")
        pas.send_keys(payload['pword'])
        pas.send_keys(Keys.RETURN)
        try:
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "aAttandance"))
            )
            aten = browser.find_element_by_id(
                "aAttandance").get_attribute("href")
            browser.get(aten)
            try:
                element = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='aspnetForm']/div[3]/div/div/div[2]/div/div/section/div/div[2]/table/tbody/tr"))
                )
                tr = len(browser.find_elements_by_xpath(
                    "//*[@id='aspnetForm']/div[3]/div/div/div[2]/div/div/section/div/div[2]/table/tbody/tr"))

                before_xpath = "//*[@id='aspnetForm']/div[3]/div/div/div[2]/div/div/section/div/div[2]/table/tbody/tr["
                aftertd_xpath = "]/td"
                data = ""
                for t_tr in range(0, tr):
                    finalxpath = before_xpath + str(t_tr) + aftertd_xpath
                    cell_text = browser.find_elements_by_xpath(finalxpath)
                    data = data+cell_text[1].text+"--"+cell_text[6].text+"\n\n"
            except:
                pass
        except:
            pass
        browser.quit()
        # send the link back
        context.bot.send_message(
            chat_id=update.message.chat_id, text=data)


def main():
    # Create updater and pass in Bot's auth key.
    updater = Updater(
        token='1499954995:AAFGlqP8E3PYA_vCACIDcgVdJwgaeFlnABA', use_context=True)
    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher
    # answer commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('username', username))
    dispatcher.add_handler(CommandHandler('password', password))
    dispatcher.add_handler(CommandHandler('attendance', attendance))
    # start the bot
    updater.start_polling()
    # Stop
    updater.idle()


if __name__ == '__main__':
    main()
