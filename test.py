from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://talaadthai.com/products?trending=today")

driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div[2]/div[1]/div/div').click()

#first Path
# //*[@id="__next"]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/div/div/img

# last Path
# //*[@id="__next"]/div[3]/div[2]/div[2]/div/div/div/div/div[74]/a/div/div/div/div/div[1]/div/div/img

# driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/div/div/img').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/div/div/img').click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-name')))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'minPrice')))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'maxPrice')))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'unit')))

# Find the elements
name1 = driver.find_element(By.CLASS_NAME, 'product-name')
minPrice = driver.find_element(By.CLASS_NAME, 'minPrice')
maxPrice = driver.find_element(By.CLASS_NAME, 'maxPrice')  # Corrected here
unit = driver.find_element(By.CLASS_NAME, 'unit')

print("Name: " + name1.text)
print("Min price: " + minPrice.text)
print("Max price: " + maxPrice.text)
print("Unit: " + unit.text)

time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div[1]/div[1]/div/div/img').click()
time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="__next"]/div[4]/div[2]/div/div/div/div/div/div/div/div[1]/div[2]/a/div[2]').click()
driver.find_element(By.CLASS_NAME,'actionZone').click()

# Close the browser
time.sleep(100)
