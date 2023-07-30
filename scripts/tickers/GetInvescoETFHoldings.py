from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import re
import json


holdings = []

browser = webdriver.Chrome()

browser.get("https://www.invesco.com/us/financial-products/etfs/holdings?audienceType=Investor&ticker=PSJ#")

table = browser.find_element(By.CLASS_NAME, "scroll-table-mobile")

stocks = table.find_elements(By.TAG_NAME, "tr")

for stock in stocks:
    html = stock.get_attribute("innerHTML")
    regex = r'.*<td class=\"text-left\" x-text=\"holding.ticker\">(\w+) </td>.*'
    val = re.search(regex, html)
    if val:
        holdings.append(val.group(1))
        
browser.quit()


data = {
    "stocks": holdings
}

with open('invesco_psj.json', 'w') as f:
    json.dump(data, f)
        

browser.quit()
