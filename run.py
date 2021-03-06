import selenium
from selenium import webdriver                              # Use selenium driver to navigate web
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
        print("Opening up messenger...")
        self.driver.get('https://messenger.com')
        sleep(5)

        # Navigate login page and insert credentials using xpaths found by website inspector
        print("Logging into messenger...")
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.click()
        email.send_keys(username)

        passwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwd.click()
        passwd.send_keys(password)

        # Log into Messenger
        login_button = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_button.click()
        print("Successfully logged into messenger!")

    # Select a conversation
    def select_conversation(self, name):
        try:
            # Find conversation by contact name
            self.driver.find_element_by_partial_link_text(name).click()
            print(f"Conversation {name} selected")
        except selenium.common.exceptions.NoSuchElementException:
            print("Cannot find conversation!")

    # Text in the current open conversation
    def text_current(self, msg, print_=True):
        if print_:
            print(f"Texting '{msg}' into the latest conversation.")
        # Navigate message line on absolute path due to random class name initialization
        msg_line = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/div[1]/div/div/div/div')
        sleep(0.1)
        msg_line.click()
        # Insert each letter individually and randomize speed to stay undetected
        for letter in msg:
            msg_line.send_keys(letter)
            sleep(random.randrange(1,3)/10)

        # Send message with random delay
        sleep(random.randrange(2,7)/10)
        send_button = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/a')
        send_button.click()

    # Text the lion king script line by line
    def lion_king(self, no_lines, dest="current"):
        # arguments: no_lines: integer of the first n lines to be sent, destination: name of destination contact,
        # select wanted conversation
        if dest != "current":
            self.select_conversation(dest)
        print(f"Texting {dest} {no_lines} lines of the lion king script.")
            # Open the script txt
        with open("lion_king.txt","r") as lines:
            n = 0
            for line in lines:
                line = line.strip()
                if (line != "") and (line[0] != "/"):   # Skip empty and commented lines
                    self.text_current(line.strip(),print_=False)
                    sleep(random.randrange(7,11)/10)
                if n > no_lines:
                    break                               # Break out of loop after no_lines lines
                n += 1
        print("Lion king was delivered!")

# Load up bot object and log in to Messenger
bot = MessengerBot()
bot.login()
