# FB Messenger Bot
An unintelligent messenger bot for Facebook Messenger implemented in Python.

## Features
- log into Messenger automatically
- select a conversation by contact name
- text into the current conversation
- text a number of lines of the Lion King movie script to a destination contact

## Libraries used
- selenium
- webdriver_manager

## Installation and Example Usage
'''
pip install selenium
pip install webdriver_manager
// Set up a 'keys.py' with 'username, password = *username*, *password*' and an empty '__init__.py' file in the parent folder
// Run the script interactively to perform methods
python -i run.py
// A bot object is initialized as 'bot' and logs into a messenger browser window
// You can now perform the methods described above on the bot
// Example: Select conversation with David
bot.select_conversation("David")
// Example: Text a message into the latest conversation
bot.text_latest(message)
// Example: Text 113 lines of lion king script to David
bot.lion_king(113, "David")
'''
