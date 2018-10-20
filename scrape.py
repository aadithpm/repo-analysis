import requests
from bs4 import BeautifulSoup
from auth_tokens import token, user, passw
import json

def get_num_repositories(url):
	request = requests.get(url)
	c = BeautifulSoup(request.content, "lxml")
	return int(c.find_all("span", "Counter")[0].contents[0])

def get_users(id = 0):
    if id == 0:
        request = requests.get("https://api.github.com/users", auth = (user, passw))
    else:
        id = str(id)
        request = requests.get("https://api.github.com/users?since="+id, auth = (user, passw))

    json_data = json.loads(request.text)
    return json_data

def make_dataset(id = 0):
    users_data = []
    since_id = id
    while 1:
        request_data = get_users(since_id)
        try:
            since_id = request_data[-1]['id']
        except:
            break
        users_data.extend(request_data)
        print(" -- Current size: {} -- Got {} users".format(str(len(users_data)), str(len(request_data))))
    return users_data    

