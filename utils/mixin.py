import random
import string
from django.conf import settings


# Base URL remove extra splash
def base_url():
    url = settings.SITE_URL
    uri = url.replace('/', '')
    return uri


# When user will create device token will automatically create random 10 digit string
letters = string.ascii_lowercase
random_device_token = ''.join(random.choice(letters) for i in range(10))


# Get average rating
def average_rating(num):
    rating = 0

    for n in num:
        rating = rating + n
    try:
        avg = rating / len(num)
        return avg
    except ZeroDivisionError:
        return str("Zero can't division...")
