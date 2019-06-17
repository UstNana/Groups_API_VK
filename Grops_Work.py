
from urllib.parse import urlencode
import requests
import pprint

OAUTH_URL = "https://oauth.vk.com/authorize"
APP_ID_1 = 6892877

auth_data = {
  "client_id": APP_ID_1,
  "display": "page",
  "scope": "friends, status",
  "response_type": "token",
  "v": 5.92
}
print("?".join((OAUTH_URL, urlencode(auth_data))))
token = "bb20fdbcdfada531594c5c105f60608a8cfc77da2580af2f4b42cc2f27df8732d98eabb931bdabe7bfbbb"

params_2 = {
  "access_token": token,
  "v": 5.92,
  "user_id": "",
  "order": "",
  "list_id": "",
  "count": "",
  "offset": "",
  "fields": "verified",
  "name_case": ""
}
response_friend = requests.get("https://api.vk.com/method/friends.get", params_2)
friend_list = response_friend.json()
print(friend_list)

tems = friend_list["response"]["items"]
params_2 = {
  "access_token": token,
  "v": 5.92,
  "user_id": "",
  "extended": 1
}
response_group = requests.get("https://api.vk.com/method/groups.get", params_2)
my_groups = response_group.json()
print (response_group.json())
my_groups_list = my_groups["response"]["items"]
print (my_groups_list)

for elements in tems:
  friend_list_2 = elements["id"]
  params_4 = {
    "access_token": token,
    "v": 5.92,
    "user_id": friend_list_2,
    "extended": 1
  }
  response_friend_group = requests.get("https://api.vk.com/method/users.getSubscriptions", params_4)
  print (response_friend_group.json())
  friend_group = response_friend_group.json()
  friend_group_list = friend_group["response"]["items"]
  print(friend_group_list)

  s = 0
  for groups in friend_group_list:
    name_groups1 = groups["name"]
  for groups in my_groups_list:
    name_groups2 = groups["name"]
    if name_groups2 == name_groups1:
      print("YES")
    else:
      s = s + 1
      print(s)
