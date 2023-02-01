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
