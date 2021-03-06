> 7 July 2021 | Day 41-  Day 44

web development( class already taken )

> 8 July 2021 | Day 45

Web scraping with Beautiful Soup
- When we need data from the website and it doesn't offer api, then we can use HTML parser like Beautiful Soup

**Beautiful Soup 4 Documentation** [link](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```python
from bs4 import BeautifulSoup
# import lxml

contents = '''
<html>
	<title>Title Ray</title>
	<body>
		<h1 id="name" class="heading">Here the Heading</h1>
		<p class="detail">Here is the first paragraph</p>
		<p>Here is the second paragraph</p>
		<a href="https://www.google.com">google</a>
		<p>
		Here is the link to amazom <a href="https://www.amazom.com">link</a>
		</p>
		<a href="https://www.github.com">github</a>
	</body>
</html>
'''

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify())

print(soup.h1)

print(soup.find_all(name="p"))

all_paragraph = soup.find_all(name="p")
for par in all_paragraph:
	print(par.getText())

heading = soup.find(name="h1", id="name")
print(heading)

detail = soup.find(name="p", class_="detail")
print(detail)
print(detail.get("class"))

shopping_url = soup.select_one(selector="p a")
print(shopping_url)

heading = soup.select(".heading")
print(heading)
```

> 9 July 2021 | Day 46

Robots.txt
- tells search engine crawlers which URLs the crawler can accesss on your site. This is used mainly to avoid overloading your site with requests.

```
URL https://www.billboard.com/robots.txt

result:
User-agent: *
Disallow: /wp/wp-admin/
Allow: /wp/wp-admin/admin-ajax.php
```

Musical Time Machine Project

> 10 July 2021 | Day 47

Create an amazom item price drop notifyier through email.

> 11 July 2021 | Day 48

Selenium Webdriver browser and Game playing bot

Download chrome driver and specify a location in your computer

- automate the browser like human.

[Selenium Documentation](https://www.selenium.dev/documentation/en/)

```python
from selenium import webdriver

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

# driver.close()   # close single tab
driver.quit()   # quit the entire program
```
Find Element 
- find element by id
- find element by name
- find element by class name
- find element by css selector
- find elemetn by xpath

Find Elements

[Cookie Clicker](https://gist.github.com/angelabauer/affb3ce61bc79ada90dea26052c27c2b)
