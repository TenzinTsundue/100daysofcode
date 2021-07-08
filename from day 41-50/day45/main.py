# scrape top 100 movies from a empireonline website and store it into a txt file

import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_list = [movie.getText() for movie in all_movies]
movies = movie_list[::-1]   # reverse the order

with open("movies.txt", mode="w") as file:
	for movie in movies:
		file.write(f"{movie}\n")


