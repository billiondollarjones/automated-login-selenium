from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Go to HerokuApp login
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

# Locate elements
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Enter credentials
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login_button.click()

# Wait and screenshot result
time.sleep(3)
driver.save_screenshot("heroku_login_result.png")

# Close browser
driver.quit()