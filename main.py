import requests
import json
from config import url, API_KEY


def get_rates():
    response = requests.get(url, params={'apikey': API_KEY})
    if response.status_code == 200:
        return json.loads(response.text)
    return None


if __name__ == '__main__':
    print(get_rates())
