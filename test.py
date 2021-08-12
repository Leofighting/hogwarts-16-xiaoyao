import requests


def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {"User-Agent": "leo"}
    cookie = {
        "name": "leo",
        "address": "Foshan"
    }
    r = requests.get(url=url, headers=header, cookies=cookie)
    print(r.request.headers)
