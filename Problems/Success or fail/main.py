import requests


def check_success(url):
    return "Success" if bool(requests.get(url)) else "Fail"

