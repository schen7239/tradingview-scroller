from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

stocks = ["XLY", "WANT", "TSLA", "PLTR"]

browser = webdriver.Chrome()

browser.get('https://www.tradingview.com/chart')

time.sleep(3)
for stock in stocks:
    main_page = browser.find_element(By.CLASS_NAME, "chart-page")

    main_page.send_keys(stock)
    time.sleep(.5)
    modal = browser.find_element(By.CLASS_NAME, "search-eYX5YvkT")

    modal.send_keys(Keys.RETURN)
    time.sleep(4)

browser.quit()
