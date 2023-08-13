import requests

url = "https://fcm.googleapis.com/fcm/send"

auth_key = "auth_key"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"key={auth_key}"
}


def send_notification(send_to, title, message):
    to = send_to
    data = {
        'title': title,
        'message': message
    }
    body = {
        'to': to,
        'data': data
    }
    response = requests.post(url, json=body, headers=headers)
    return response
