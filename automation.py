import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

driver = uc.Chrome()

driver.get('http://www.google.com/')

time.sleep(5)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(5)

try:
    driver.quit()
except Exception:
    pass