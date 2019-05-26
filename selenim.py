import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
  
browser = webdriver.Firefox()
browser.get("https://www.irctc.co.in/nget/train-search")

# username = browser.find_element_by_id("user_name")
# password = browser.find_element_by_id("password")
# from_station   = browser.find_element_by_id("origin")

from_station = browser.find_element_by_xpath('//*[@id="origin"]/span/input')
to_station = browser.find_element_by_xpath('//*[@id="destination"]/span/input')
date = browser.find_element_by_xpath('//input[@placeholder="Journey Date(dd-mm-yyyy)*"]')

from_station.click()
from_station.send_keys("RNC")
time.sleep(1)
from_station.send_keys(Keys.RETURN)

to_station.click()
to_station.send_keys("NDLS")
time.sleep(1)
to_station.send_keys(Keys.RETURN)

for i in range(10):
    date.send_keys(Keys.BACKSPACE)
date.send_keys('30-05-2019')
time.sleep(1)
date.send_keys(Keys.RETURN)

time.sleep(5)

# element = browser.find_elements_by_xpath("//span")
# browser.execute_script("arguments[0].style.visibility='hidden'", element)

time.sleep(2)
found = browser.find_element_by_xpath('//a[@id="T_12453"]/../../../../div[3]/div[2]/div/div/button')
# found = browser.find_elements_by_xpath('//button[@id="check-availability"]')[0]
found.send_keys(Keys.RETURN)


time.sleep(2)
book_now = browser.find_element_by_xpath('//button[@class="b1"]')
# book_now.send_keys(Keys.RETURN)
print(len(book_now))


  