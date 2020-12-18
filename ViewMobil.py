from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Expected data yang akan dicek
expected_data = "http://localhost/rental_mobil/admin/mobil"

# Script Test Case
try:
    driver = webdriver.Chrome("C:/Setup-Folder/Selenium_Grid/chromedriver")
    driver.maximize_window()
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

    # Login Success
    # Go To Data Master -> Mobil

    # Find Navigation Element
    e = driver.find_element(
        By.XPATH, "//a[contains(@href, 'http://localhost/rental_mobil/admin/mobil')]")
    e.click()

    # Asserting Condition
    # Jika URL Diarahkan ke Halaman Utama Maka Assert True
    # Jika URL Tidak Berubah Assert False
    try:
        assert driver.current_url == expected_data
        print("Assertion for Login Success!")
    except AssertionError:
        print("Assertion for Login Failed!")

    time.sleep(2)

# Close Driver
finally:
    if driver is not None:
        driver.close()
