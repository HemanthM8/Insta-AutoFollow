from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSOWRD"
TARGET_ACCOUNT = "cbitosc"

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")

wait = WebDriverWait(driver, 15)

username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(5)

driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
time.sleep(5)

try:
    follow_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Follow']")))
    follow_button.click()
    print("Followed the account.")
except:
    print("Already following.")

try:
    time.sleep(3)
    stats = driver.find_elements(By.XPATH, "//ul[contains(@class, 'xieb3on')]/li")
    posts = stats[0].text.split(" ")[0]
    followers = stats[1].text.split(" ")[0]
    following = stats[2].text.split(" ")[0]


    profile_data = {
        "Profile": TARGET_ACCOUNT,
        "Posts": posts,
        "Followers": followers,
        "Following": following,
     }

    filename = f"{TARGET_ACCOUNT}_profile.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in profile_data.items():
            f.write(f"{key}: {value}\n")
        print(f"Saved profile data to {filename}")
except Exception as e:
    print("Error extracting data:", e)

driver.quit()
