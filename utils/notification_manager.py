import requests
from django.conf import settings

url = "https://onesignal.com/api/v1/notifications/"
authorization = "authorization_KEY"
APP_ID = "YOUR_APP_ID"
app_name = "HerculesDev"

headers = {
    "accept": "text/plain",
    "Content-Type": "application/json",
    "Authorization": f"Basic {authorization}"
}


# The notification will throw all users
def send_notification_to_all(title, message, icon=None, picture=None):
    body = {
        "app_id": APP_ID,
        "app_name": app_name,
        "included_segments": ['Subscribed Users'],
        "large_icon": icon,
        "big_picture": picture,
        "headings": {"en": title},
        "contents": {"en": message},
    }

    return requests.post(url, json=body, headers=headers)


# The notification will throw for single user
def send_notification_single_user(device_token, title, message, icon=None, picture=None):
    body = {
        "app_id": APP_ID,
        "app_name": app_name,
        "include_player_ids": [device_token],
        "large_icon": icon,
        "big_picture": picture,
        "headings": {"en": title},
        "contents": {"en": message},
    }

    return requests.post(url, json=body, headers=headers)
