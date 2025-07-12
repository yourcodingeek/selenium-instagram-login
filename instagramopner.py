from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Username and password
username = "username"  # Your username
password = "your-own-password"  # Your password

# Open safari
driver = webdriver.Safari()

try:
    # Go to instagram
    driver.get("https://www.instagram.com")

    # Wait for username and fill it
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.clear()  # Clear field
    username_field.send_keys(username)
    print("Username entered:", username)
    time.sleep(2)  # Wait

    # Şifre alanını bekle ve doldur
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.clear()  # Clear field
    for char in password:
        password_field.send_keys(char)
        time.sleep(0.2)
    print("Password entered:", password)
    time.sleep(3)

    # Click login
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()
    print("Login button clicked")

    # Wait for login process
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search input']"))
        )
        print("Login successful, homepage loaded")
    except:
        print("Login failed, page did not change")

    print("Browser left open. You can close it manually.")
    time.sleep(30)

except Exception as e:
    print("An error occurred:", str(e))