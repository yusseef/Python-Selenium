from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox() 
driver.get("http://127.0.0.1:8000/home/sign-up")
driver.implicitly_wait(5)
element = driver.find_element('id', 'Signup')
#element.click()

#check_element = driver.find_element("id", "test")

#print(f"the text is {check_element.text}")

WebDriverWait(driver, 25).until(
    EC.text_to_be_present_in_element(
        (By.ID, 'test'), 
        'please fill all fields'
    )
)
