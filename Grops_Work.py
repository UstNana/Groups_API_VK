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
token = "dde5b29d513fdd7c9d5f0e7127a83bce463a4fdffad807f2a363989cb56f080a44fa9a66a50346d06c22f"

class Group:

  def __init__(self, access_token):
    self.access_token = access_token


  def __str__(self):
    return "{}".format(self.access_token)

  def get_friends_info(self):
    params_1 = {
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
    response_friend = requests.get("https://api.vk.com/method/friends.get", params_1)
    friend_list = response_friend.json()
    tems = friend_list["response"]["items"]

    for elements in tems:
      friend_list_2 = elements["id"]
      params_4 = {
        "access_token": token,
        "v": 5.92,
        "user_id": friend_list_2,
        "extended": 1
      }
      response_friend_group = requests.get("https://api.vk.com/method/users.getSubscriptions", params_4)
      friend_group = response_friend_group.json()
      friend_group_list = friend_group["response"]["items"]
      params_2 = {
        "access_token": token,
        "v": 5.92,
        "user_id": "",
        "extended": 1
      }
      response_group = requests.get("https://api.vk.com/method/groups.get", params_2)
      my_groups = response_group.json()

      my_groups_list = my_groups["response"]["items"]

      sum = 0
      for groups in friend_group_list:
        name_groups_friends = groups["name"]
      for groups in my_groups_list:
        my_name_groups = groups["name"]
        if my_name_groups == name_groups_friends:
          return YES
        else:
          sum = sum + 1
          return sum

user1 = Group(token)

print(user1.get_friends_info())
