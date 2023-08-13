import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(10)

finally:
    browser.quit()