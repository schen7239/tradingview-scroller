from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
from pynput import keyboard




class KeyHandler:
    def __init__(self):
        self.last_key_pressed = None
        pass
    def on_key_press(self, key):
        if (key == keyboard.Key.left):
            self.set_last_key_pressed(-1)
        elif(key == keyboard.Key.right):
            self.set_last_key_pressed(1)
        elif(key == keyboard.Key.esc):
            self.set_last_key_pressed("ESCAPE")
        else:
            self.set_last_key_pressed(None)
    
    def get_last_key_pressed(self):
        return self.last_key_pressed
    def set_last_key_pressed(self, val):
        self.last_key_pressed = val

class TradingViewWatcher:
    def __init__(self, file, format = "JSON") -> None:
        self.key_handler = KeyHandler()
        if format == "JSON":
            f = open(file)
            self.stocks =  json.load(f)["stocks"]
    
    def login(self):
        pass
    
    def run(self, position = 0):
        list_size = len(self.stocks)
        browser = webdriver.Chrome()
        
        browser.get('https://www.tradingview.com/chart')
        
        listener = keyboard.Listener(on_press=self.key_handler.on_key_press)
        listener.start()
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
        listener.stop()    
        browser.quit()
