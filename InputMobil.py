from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Expected data yang akan diinput ke sistem
expected_data = ["Avanza", "B 1234 ABC", "Putih", "2015"]

# Jumlah kolom yang akan diinput
n_col = len(expected_data)

# Pengecekan pada Assert untuk Test Case


def AssertData(n_col, expected_data, actual_data):
    for i in range(0, n_col):
        if (expected_data[i] != actual_data[i]):
            return False
    return True


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

    time.sleep(2)

    # Find Input Mobil Button
    e = driver.find_element(
        By.XPATH, "//a[contains(@href, 'http://localhost/rental_mobil/admin/mobil_add')]")
    e.click()

    # Input Mobil Form
    e = driver.find_element(By.NAME, "merk")
    e.send_keys(expected_data[0])

    e = driver.find_element(By.NAME, "plat")
    e.send_keys(expected_data[1])

    e = driver.find_element(By.NAME, "warna")
    e.send_keys(expected_data[2])

    e = driver.find_element(By.NAME, "tahun")
    e.send_keys(expected_data[3])

    time.sleep(2)

    # Submit Form
    e = driver.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    e.click()

    time.sleep(2)

    # Cek Elemen Data pada Row Table yang Terakhir
    actual_data = []
    for i in range(n_col):
        # Input ke dalam array setiap table column yang ingin diambil datanya
        actual_data.append(driver.find_element(
            By.XPATH, "//tr[last()]/td[" + str(i+1) + "]").text)

    # Asserting Condition
    # Jika data yang diinsert sama dengan yang ada pada table column, maka Test Sukses
    # Jika tidak, Test Gagal
    try:
        assert AssertData(n_col, expected_data, actual_data)
        print("Assertion for Input Mobil Success!")
    except AssertionError:
        print("Assertion for Input Mobil failed!")

# Close Driver
finally:
    if driver is not None:
        driver.close()
