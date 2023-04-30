from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        time.sleep(5)

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login_btn.click()

        fb_btn = self.driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
        fb_btn.click()

        time.sleep(5)

        



        # switch to login popup

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])


bot = TinderBot()
bot.login()