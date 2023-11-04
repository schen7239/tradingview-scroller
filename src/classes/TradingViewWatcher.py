from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

from .KeyboardHandler import KeyboardHandler
from ..constants.TradingViewWatcherConstants import FileTypes, ScrollType

class TradingViewWatcher:
    def __init__(self, file, format = FileTypes.JSON, scroll_type = ScrollType.MANUAL, position = 0) -> None:
        self.scroll_type = scroll_type
        match scroll_type:
            case ScrollType.MANUAL:
                self.key_handler = KeyboardHandler()
            case ScrollType.LAZY:
                self.key_handler = None
            case default:
                raise ValueError("INVALID SCROLL_TYPE")
        match format:
            case FileTypes.JSON:
                f = open(file)
                self.stocks =  json.load(f)["stocks"]
            case default:
                raise NotImplementedError("ONLY JSON WORKS")
        self.position = position if self.isPositionValid(position) else 0
    
    def login(self):
        pass
    
    def isPositionValid(self, position) -> None:
        stock_len = len(self.stocks)
        
        if position < 0 or position >= stock_len:
            print("Position invalid starting at 0")
            return False
        return True
        
    
    def run_lazy_scrolling(self):
        browser = webdriver.Chrome()
        
        browser.get('https://www.tradingview.com/chart')
        while True:
            time.sleep(2)
            browser.find_element(By.ID, "header-toolbar-symbol-search").click()
            modal = browser.find_element(By.CLASS_NAME, "search-ZXzPWcCf")
            time.sleep(0.5)
            modal.send_keys(self.stocks[self.position])
            modal.send_keys(Keys.RETURN)
            self.position += 1
    
    def run_manual_scrolling(self):
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
            
            if self.position == 0 and self.key_handler.get_last_key_pressed() < 0:
                self.key_handler.set_last_key_pressed(None)
                continue
            
            if self.position == list_size - 1 and self.key_handler.get_last_key_pressed() > 0:
                self.key_handler.set_last_key_pressed(None)
                continue
            
            browser.find_element(By.ID, "header-toolbar-symbol-search").click()
            modal = browser.find_element(By.CLASS_NAME, "search-ZXzPWcCf")
            self.position = self.position + self.key_handler.get_last_key_pressed()
            print(self.position)
            time.sleep(0.2)
            modal.send_keys(self.stocks[self.position])
            modal.send_keys(Keys.RETURN)
            self.key_handler.set_last_key_pressed(None)
        self.key_handler.remove_listener()
        browser.quit()
        
    
    def run(self):
        match self.scroll_type:
            case ScrollType.LAZY:
                self.run_lazy_scrolling()
            case ScrollType.MANUAL:
                self.run_manual_scrolling()
            case default:
                raise NotImplementedError("SOMETHING WRONG WITH CLASS. SHOULD BE CAUGHT EARLIER")
