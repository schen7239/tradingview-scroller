from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import re
import json


russell_2000_holdings = []

browser = webdriver.Chrome()

browser.get("https://www.ishares.com/us/products/272532/?cid=ppc:ish_us:ish_us_br_megatrends_exponentialtechnology_nonproduct_ei_phrase:google:brand_nonprod:ei&gclid=Cj0KCQjwqs6lBhCxARIsAG8YcDi7NldJlL48p-3uIe1df8Ebrw3kHtR8DvgS0Dgf5FxMBwiHTdJhHDcaAoxlEALw_wcB&gclsrc=aw.ds")
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
    "sp500_holdings": russell_2000_holdings
}

with open('./holdings/XT_ishares.json', 'w') as f:
    json.dump(data, f)
        

browser.quit()
