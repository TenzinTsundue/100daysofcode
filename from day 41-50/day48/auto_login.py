# Automatic login to Instagram

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.instagram.com/accounts/login/")

# username_field = driver.find_element_by_name("username")
# username_field.send_keys("yourusername")

# password_field = driver.find_element_by_name("password")
# password_field.send_keys("yourpassword")

# login_button = driver.find_element_by_class_name("sqdOP  L3NKy   y3zKF     ")
# login_button.click()

# search.send_keys(Keys.ENTER

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("username")
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("password")
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

# driver.quit()