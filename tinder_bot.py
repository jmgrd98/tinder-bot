from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from login_details import email, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        cookies_accept_button = self.driver.find_element(By.XPATH, '//*[@id="s-407411262"]')
        cookies_accept_button.click()

        time.sleep(5)

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login_btn.click()

        time.sleep(5)


        fb_btn = self.driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
        fb_btn.click()

        time.sleep(5)
        
        # switch to login popup 

        base_window = self.driver.window_handles[0]
        fb_popup_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_popup_window)

        # login to fb

        email_in = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_in.send_keys(email)

        pw_in = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pw_in.send_keys(password)

        fb_login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
        fb_login_btn.click()

        time.sleep(5)

        self.driver.switch_to.window(base_window)

        accept_loc_btn = self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
        accept_loc_btn.click()

        time.sleep(50)





bot = TinderBot()
bot.login()