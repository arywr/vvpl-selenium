from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome("C:/Setup-Folder/Selenium_Grid/chromedriver")
    driver.get("http://localhost/rental_mobil/")
    time.sleep(2)

    # Input Username
    e = driver.find_element(By.ID, "inputUname")
    e.send_keys("admin")

    time.sleep(1)

    # Input Password
    e = driver.find_element(By.ID, "inputPassword")
    e.send_keys("admin")
    time.sleep(2)

    # Login Button Click
    e = driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block")
    e.submit()
    time.sleep(2)

finally:
    if driver is not None:
        driver.close()
