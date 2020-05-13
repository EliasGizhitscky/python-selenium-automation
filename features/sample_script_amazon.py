from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')
sleep(1)

sell_link = driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[text()='Sell']").click()
sleep(1)

button = driver.find_element(By.XPATH, "//*[@id=\"eventColor\"]/div[3]/div/div/div[1]/div/div[1]/div[3]/div/div/a").click()
sleep(1)

assert 'Get started selling on Amazon' in driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
sleep(1)

driver.quit()