from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/checkout-step-one.html")

try:
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("Test réussi : Connexion pour 'standard_user' validée.")

except Exception as e:
    print("Test échoué :", e)

finally:
    driver.quit()








