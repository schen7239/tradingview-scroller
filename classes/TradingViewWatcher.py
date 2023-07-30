from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
from .KeyboardHandler import KeyboardHandler

class TradingViewWatcher:
    def __init__(self, file, format = "JSON") -> None:
        self.key_handler = KeyboardHandler()
        if format == "JSON":
            f = open(file)
            self.stocks =  json.load(f)["stocks"]
    
    def login(self):
        pass
    
    def run(self, position = 0):
        list_size = len(self.stocks)
        browser = webdriver.Chrome()
        
        browser.get('https://www.tradingview.com/chart')
        self.key_handler.init_listener()
        while True:
            while self.key_handler.get_last_key_pressed() is None:
                time.sleep(0.1)
                pass
            if (self.key_handler.get_last_key_pressed() == "ESCAPE"):
                break
            
            if position == 0 and self.key_handler.get_last_key_pressed() < 0:
                self.key_handler.set_last_key_pressed(None)
                continue
            
            if position == list_size - 1 and self.key_handler.get_last_key_pressed() > 0:
                self.key_handler.set_last_key_pressed(None)
                continue
            
            browser.find_element(By.ID, "header-toolbar-symbol-search").click()
            modal = browser.find_element(By.CLASS_NAME, "search-ZXzPWcCf")
            position = position + self.key_handler.get_last_key_pressed()
            time.sleep(0.2)
            modal.send_keys(self.stocks[position])
            modal.send_keys(Keys.RETURN)
            self.key_handler.set_last_key_pressed(None)
        self.key_handler.remove_listener()
        browser.quit()
