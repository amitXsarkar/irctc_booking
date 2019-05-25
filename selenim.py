from selenium import webdriver
from selenium.common.exceptions import TimeoutException
  
browser = webdriver.Firefox()
browser.get("http://127.0.0.1:5000/login")

username = browser.find_element_by_id("user_name")
password = browser.find_element_by_id("password")
submit   = browser.find_element_by_class_name("btn")
  
username.send_keys("a")
password.send_keys("a")
  

submit.click()
  

wait = WebDriverWait( browser, 5 )
  
try:
    page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)
except TimeoutException:
    self.fail( "Loading timeout expired" )
  
# self.assertEqual(browser.current_url,correct_page,msg = "Successful Login")