# interaction with wikipedia

from selenium import webdriver

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_articles = driver.find_element_by_css_selector("#articlecount a")
print(total_articles.text)

total_articles.click()

driver.quit()