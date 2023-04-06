from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

class TradingViewWatcher:
    def __init__(self, file, format = "JSON") -> None:
        if format == "JSON":
            f = open(file)
            self.stocks =  json.load(f)["stocks"]
    
    def run(self, position = 0):
        browser = webdriver.Chrome()

        browser.get('https://www.tradingview.com/chart')
        
        time.sleep(3)
        for stock in self.stocks[position:]:
            browser.find_element(By.ID, "header-toolbar-symbol-search").click()
            time.sleep(1)
            modal = browser.find_element(By.CLASS_NAME, "search-eYX5YvkT")
            modal.send_keys(stock)
            modal.send_keys(Keys.RETURN)
            time.sleep(4)

        browser.quit()
