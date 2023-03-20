from selenium import webdriver


driver = webdriver.Firefox() 
driver.get("http://127.0.0.1:8000/home/sign-up")
driver.implicitly_wait(5)
element = driver.find_element('id', 'Signup')
element.click()