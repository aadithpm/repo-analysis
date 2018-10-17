import requests
from bs4 import BeautifulSoup

def get_num_repositories(name):
	url = "https://github.com/" + name
	request = requests.get(url)
	c = BeautifulSoup(request.content, "lxml")
	return int(c.find_all("span", "Counter")[0].contents[0])

