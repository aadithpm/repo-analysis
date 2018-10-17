import requests
from bs4 import BeautifulSoup
import json

def get_num_repositories(url):
	request = requests.get(url)
	c = BeautifulSoup(request.content, "lxml")
	return int(c.find_all("span", "Counter")[0].contents[0])

def get_users(id=0):
    if id == 0:
        request = requests.get("https://api.github.com/users")
    else:
        id = str(id)
        request = requests.get("https://api.github.com/users?since="+id)
    json_data = json.loads(request.text)
    return json_data

