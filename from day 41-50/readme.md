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
