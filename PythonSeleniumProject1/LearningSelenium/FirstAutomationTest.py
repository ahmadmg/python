from selenium import webdriver

# Selenium will automatically handle downloading the correct driver
driver = webdriver.Chrome()

driver.get("https://www.google.com")
print(driver.title)
driver.quit()