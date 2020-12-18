from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Expected data yang akan diinput ke sistem
expected_data = ["Dummy Name", "Jl.Dayeuhkolot, Bandung",
                 "08979512412", "69219497194"]

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
    # Go To Data Master -> Kostumer

    # Find Navigation Element
    e = driver.find_element(
        By.XPATH, "//a[contains(@href, 'http://localhost/rental_mobil/admin/kostumer')]")
    e.click()

    time.sleep(2)

    # Find Input Kostumer Button
    e = driver.find_element(
        By.XPATH, "//a[contains(@href, 'http://localhost/rental_mobil/admin/kostumer_add')]")
    e.click()

    # Input Kostumer Form
    e = driver.find_element(By.NAME, "nama")
    e.send_keys(expected_data[0])

    e = driver.find_element(By.NAME, "alamat")
    e.send_keys(expected_data[1])

    e = driver.find_element(
        By.CSS_SELECTOR, "input[type='radio'][value='L']")
    e.click()
    expected_data.append(e.get_attribute("value"))

    e = driver.find_element(By.NAME, "hp")
    e.send_keys(expected_data[2])

    e = driver.find_element(By.NAME, "ktp")
    e.send_keys(expected_data[3])

    time.sleep(2)

    # Submit Form
    e = driver.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    e.click()

    time.sleep(2)

    # Cek Elemen Data pada Row Table yang Terakhir
    actual_data = []

    # Menyusun Ulang Array sesuai Format Tabel
    reorder = [0, 4, 2, 3, 1]
    expected_data[:] = [expected_data[i] for i in reorder]

    for i in range(n_col):
        # Input ke dalam array setiap table column yang ingin diambil datanya
        e = driver.find_element(
            By.XPATH, "//tr[last()]/td[" + str(i+1) + "]").text.split('\n')
        for data in e:
            actual_data.append(data)

    # Asserting Condition
    # Jika data yang diinsert sama dengan yang ada pada table column, maka Test Sukses
    # Jika tidak, Test Gagal
    try:
        assert AssertData(n_col, expected_data, actual_data)
        print("Assertion for Input Kostumer Success!")
    except AssertionError:
        print("Assertion for Input Kostumer failed!")

# Close Driver
finally:
    if driver is not None:
        driver.close()
