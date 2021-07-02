import requests
from datetime import datetime

USERNAME = "tsundue"
TOKEN = "4j5h3kj4h5k3iu43g"
GRAPH_ID = "graph1"

# To create user namea and token
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

# response =requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# To create a graph
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
	"id": GRAPH_ID,
	"name": "Cycling Graph",
	"unit":"km",
	"type":"float",
	"color":"shibafu",
}

headers = {
	"X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# To put a pixel
pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now().strftime("%Y%m%d")

pixel_data = {
	"date":today,
	"quantity": "9.0",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# To put pixel or Update pixel
update_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/today'

update_pixel_data = {
	"quantity": "22.5",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)

# To delete a pixel
# response = requests.delete(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)
