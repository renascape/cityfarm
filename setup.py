import datetime
import random


def current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def DHT_result():
    DHT = random.randint(0, 100)
    return DHT

