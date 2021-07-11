from selenium import webdriver

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Get price for an amazon item
driver.get("https://www.amazon.in/Apple-MacBook-Chip-13-inch-512GB/dp/B08N6DXX1V/ref=sr_1_1?dchild=1&keywords=m1+macbook+air&qid=1625980175&sr=8-1")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

driver.get("https://www.python.org/")
search_bar = driver.find_element_by_name("q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

help = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[1]/a')
print(help.text)

driver.quit()   # quit the entire program

