from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Use ChromeDriverManager to automatically get the correct driver
web = webdriver.Chrome() # Changed line
web.get('https://forms.gle/uYULuxM5Ev3spTaD6')
time.sleep(5)


name = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys("Chandhini")

email = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
email.send_keys("chandhini@gmail.com")

RadioButton=web.find_element(By.XPATH,'//*[@id="i16"]/div[3]/div')
RadioButton.click()

submit=web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
submit.click()



web.quit()
