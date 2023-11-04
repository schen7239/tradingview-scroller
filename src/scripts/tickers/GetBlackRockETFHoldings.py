from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import re
import json


russell_2000_holdings = []

browser = webdriver.Chrome()

browser.get("https://www.ishares.com/us/products/308878/ishares-genomics-immunology-and-healthcare-etf")
time.sleep(10)

stocks_even = browser.find_elements(By.CLASS_NAME, "even")
stocks_odd = browser.find_elements(By.CLASS_NAME, "odd")

stocks = stocks_even + stocks_odd

for stock in stocks:
    html = stock.get_attribute("innerHTML")
    print(html)
    regex = r'<td class=\" colTicker col1\">(\w+)</td>'
    val = re.match(regex, html)
    if val:
        russell_2000_holdings.append(val.group(1))

data = {
    "stocks": russell_2000_holdings
}

with open('./holdings/genomics.json', 'w') as f:
    json.dump(data, f)
        

browser.quit()
