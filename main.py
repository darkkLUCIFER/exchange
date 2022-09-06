from fileinput import filename

import requests
import json
from config import url, API_KEY


def get_rates():
    response = requests.get(url, params={'apikey': API_KEY})
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(file_name, rates):
    with open(f'archive/{file_name}.json', 'w') as f:
        f.write(json.dumps(rates))


if __name__ == '__main__':
    data = get_rates()
    archive(data['timestamp'], data['rates'])
