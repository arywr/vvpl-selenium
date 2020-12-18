from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Expected data yang akan diinput ke sistem
expected_data = ["Xenia", "B 7890 OPQ", "Hitam", "2017"]

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

    # Login System

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

    # Ambil Data Pertama pada List Mobil
    e = driver.find_element(
        By.XPATH, "//*[@id='dataTable']/tbody/tr[1]/td[7]/a[1]").click()

    # Input Mobil Form
    e = driver.find_element(By.NAME, "merk")
    e.clear()
    e.send_keys(expected_data[0])

    e = driver.find_element(By.NAME, "plat")
    e.clear()
    e.send_keys(expected_data[1])

    e = driver.find_element(By.NAME, "warna")
    e.clear()
    e.send_keys(expected_data[2])

    e = driver.find_element(By.NAME, "tahun")
    e.clear()
    e.send_keys(expected_data[3])

    time.sleep(2)

    # Submit Form
    e = driver.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    e.click()

    time.sleep(2)

    # Cek Elemen Data pada Row Table yang Diubah
    actual_data = []
    for i in range(n_col):
        # Input ke dalam array setiap table column yang ingin diambil datanya
        actual_data.append(driver.find_element(
            By.XPATH, "//tr[1]//td[" + str(i+2) + "]").text)

    # Asserting Condition
    # Jika data yang diedit sama dengan yang ada pada table column, maka Test Sukses
    # Jika tidak, Test Gagal
    try:
        assert AssertData(n_col, expected_data, actual_data)
        print("Assertion for Edit Mobil Success!")
    except AssertionError:
        print("Assertion for Edit Mobil failed!")

# Close Driver
finally:
    if driver is not None:
        driver.close()
