import sys
import requests
from os import rename


def greet(whats_yo_name_bro):
    greetthenibba = "Hella feelin good vibes yo ,{}".format(whats_yo_name_bro)
    return greetthenibba


r = requests.get("https://coreyms.com")
print(r.status_code)
