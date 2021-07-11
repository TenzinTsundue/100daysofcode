# python.org upcoming evernt to dictionary 

from selenium import webdriver

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

events = {}

#time and name
for i in range(1,6):
	date = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
	aritcal_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
	events[f'{i-1}'] = {
		'time': date.text, 
		'name': aritcal_name.text
	}

print(events)

driver.quit()