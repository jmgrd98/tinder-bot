from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_details import email, password
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.common.exceptions import TimeoutException

class TinderBot():
    def __init__(self):
        s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.wait = WebDriverWait(self.driver, 10)

    def click_when_present(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def login(self):
        self.driver.get('https://tinder.com')

        # Accept Cookies
        self.click_when_present('/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
        self.click_when_present('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        self.fb_login()

        # Handle post-login popups
        popups_xpath = [
            '/html/body/div[2]/main/div/div/div/div[3]/button[1]',
            '/html/body/div[2]/main/div/div/div/div[3]/button[1]',
            '/html/body/div[2]/main/div/div/div/div[3]/button[1]'
        ]
        for popup in popups_xpath:
            try:
                self.click_when_present(popup)
            except:
                print(f"No popup for {popup}")

    def fb_login(self):
        self.click_when_present('/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        fb_popup_window = self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()

        self.driver.switch_to.window(self.driver.window_handles[0])

    def swipe(self, direction):
        body = self.driver.find_element(By.XPATH, '//*[@id="Tinder"]/body')
        if direction == 'right':
            body.send_keys(Keys.ARROW_RIGHT)
        elif direction == 'left':
            body.send_keys(Keys.ARROW_LEFT)

    # def wait_for_next_profile(self):
    #     try:
    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, 'SOME XPATH THAT INDICATES A NEW PROFILE'))
    #         )
    #     except TimeoutException:
    #         print("Timeout waiting for next profile.")
    #         return False
    #     return True

    def auto_swipe(self, swipe_direction='right'):
        while True:
            try:
                self.swipe(swipe_direction)
                
                # Wait for the new profile to load
                if not self.wait_for_next_profile():
                    print("Failed to load next profile, retrying...")
                    continue
                
            except TimeoutException:
                print("Timeout Exception Occurred")
                try:
                    self.close_match()  # only close the match if there is one
                except TimeoutException:
                    print("No match modal to close")
                continue  # continue to the next iteration even if there's an error
            except Exception as e:
                print(f"Other exception: {e}")

    def send_message_to_match(self, match_name, message):
        try:
            match_xpath = f"//span[text()='{match_name}']"
            match_elem = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/aside/nav[2]/div/div/div/div[3]/div[1]/ul[1]/li[3]/a")))
            match_elem.click()

            # Locate the message input box and send the message
            message_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/main/div/div[2]/form/textarea')))
            message_input.click()
            sleep(3)
            for char in message:
                message_input.send_keys(char)
                sleep(0.1)
            message_input.send_keys(message)
            message_input.send_keys(Keys.RETURN)
            
        except TimeoutException:
            print(f"Failed to send message to {match_name}")
            print(TimeoutException)

    def close_match(self):
        self.click_when_present('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')

    

if __name__ == '__main__':
    bot = TinderBot()
    bot.login()
    bot.send_message_to_match("Mariana", "Oi, tudo bem?")
    # bot.auto_swipe('right')
    
