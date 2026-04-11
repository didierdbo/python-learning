import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = uc.Chrome()
print(driver.name)
#driver.maximize_window()
driver.get('https://www.qaplayground.com/practice/forms')

time.sleep(5)

# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "email").send_keys("john@example.com")
driver.find_element(By.ID, "phone").send_keys("9876543210")
driver.find_element(By.ID, "city").send_keys("Mumbai")

driver.find_element(By.ID, "dob").send_keys("1995-06-15")

gender_el = driver.find_element(By.ID, "gender-male")
driver.execute_script("arguments[0].click();", gender_el)
assert gender_el.is_selected()

driver.find_element(By.CSS_SELECTOR, "[data-testid='select-country']").click()
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@role='option'][contains(.,'India')]"))
).click()


driver.find_element(By.ID, "interest-selenium").click()
driver.find_element(By.ID, "interest-playwright").click()
assert driver.find_element(By.ID, "interest-selenium").get_attribute("data-state") == "checked"

driver.find_element(By.ID, "password").send_keys("secret123")
driver.find_element(By.ID, "confirmPassword").send_keys("secret123")

driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "submitFormBtn").click()

assert WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "formSuccessMsg"))
).is_displayed()
submittedName = driver.find_element(By.ID, "submittedName").text
assert "John" in submittedName, "John not found in submittedName"
assert "Doe" in submittedName, "Doe not found in submittedName"

time.sleep(5)

try:
    driver.quit()
except Exception:
    pass