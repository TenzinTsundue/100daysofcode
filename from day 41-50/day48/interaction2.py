# interaction with wikipedia

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
total_articles = driver.find_element_by_css_selector("#articlecount a")

# click on an item
# total_articles.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()