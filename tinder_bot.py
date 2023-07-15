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

        time.sleep

        cookies_accept_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
        cookies_accept_button.click()

        time.sleep(3)

        login_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()

        time.sleep(3)

        self.fb_login()
 
        time.sleep(3)

        try:
            allow_location_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
            allow_location_button.click()
        except:
            print('no location popup')

        time.sleep(300)

        try:
            use_tinder_button = self.driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
            use_tinder_button.click()

        except:
            print('no tinder popup')

        try:
            notifications_button = self.driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
            notifications_button.click()
        except:
            print('no notification popup')

        time.sleep(10)

    
    def fb_login(self):
        fb_btn = self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        fb_btn.click()

        time.sleep(3)

        base_window = self.driver.window_handles[0]
        fb_popup_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_popup_window)

        email_in = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_in.send_keys(email)

        pw_in = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pw_in.send_keys(password)

        fb_login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
        fb_login_btn.click()

        self.driver.switch_to.window(base_window)




bot = TinderBot()
bot.login()