from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

article = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in article:
	text = article_tag.getText()
	article_texts.append(text)
	link = article_tag.get("href")
	article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)

# find the highest upvote article
largerst_number = max(article_upvote)
largerst_number_index = article_upvote.index(largerst_number)
print(article_texts[largerst_number_index])
print(article_links[largerst_number_index])

