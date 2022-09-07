import requests
import json
from config import url, API_KEY, rules
from mail import send_smtp_email


def get_rates():
    """
    send a get request to the fixer.io api and get list of rates
    :return: request.response instance
    """
    response = requests.get(url, params={'apikey': API_KEY})
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(file_name, rates):
    """
    get file_name and rates and save them into the archive
    :param file_name:
    :param rates:
    :return: None
    """
    with open(f'archive/{file_name}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    """
    get timestamp and rates and check if there is selected_rates and then send email through smtp
    :param timestamp:
    :param rates:
    :return: None
    """
    subject = f'{timestamp} rates'

    if rules['selected_rates'] is not None:
        tmp = dict()
        for exc in rules['selected_rates']:
            tmp[exc] = rates[exc]
        rates = tmp

    text = json.dumps(rates)

    send_smtp_email(subject, text)


if __name__ == '__main__':
    data = get_rates()

    # if you want to customize, got to config.py
    if rules['archive']:
        archive(data['timestamp'], data['rates'])
    if rules['send_mail']:
        send_mail(data['timestamp'], data['rates'])
