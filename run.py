from selenium import webdriver                              # Use selenium to navigate web
from webdriver_manager.chrome import ChromeDriverManager    # Keep driver accessible
from time import sleep                                      # Waiting for website loading
import random                                               # To randomize activity
import sys
sys.path.insert(0, '../')                                   # Join path for login details

# Store username and password in a keys.py file in the parent folder's directory
from keys import username, password

class MessengerBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) # Install Chrome driver if necessary

    # Log into Facebook Messenger
    def login(self):
        # Open Messenger and wait for website to load
        self.driver.get('https://messenger.com')
        sleep(5)

        # Navigate login page and insert credentials using xpaths found by website inspector
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.click()
        email.send_keys(username)

        passwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwd.click()
        passwd.send_keys(password)

        # Log into Messenger
        login_button = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_button.click()

# Load up bot object and log into Messenger
bot = MessengerBot()
bot.login()
