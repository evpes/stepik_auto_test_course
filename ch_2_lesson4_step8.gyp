from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
    button = browser.find_element_by_id('book')
    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_id('answer'))
    x = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_id('solve').click()

    
    
finally:
    time.sleep(30)
    browser.quit()