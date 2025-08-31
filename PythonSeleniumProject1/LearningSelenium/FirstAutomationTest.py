import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "C:\\browserdriver\\chrome-win64\\chrome.exe"
service_object = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service_object)
driver.get("https://www.python.org")
print(driver.title)
time.sleep(10)

driver.close()