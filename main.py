import requests
from config import url, API_KEY


def get_rates():
    response = requests.get(url, params={'apikey': API_KEY})
    json_info = response.text
    print(json_info)


if __name__ == '__main__':
    get_rates()
