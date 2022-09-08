from datetime import datetime

import requests
import json

from khayyam import JalaliDatetime

from config import url, API_KEY, rules
from mail import send_smtp_email
from notification import send_sms


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
    now = JalaliDatetime(datetime.now()).strftime("%Y-%B-%d %A %H:%M")
    subject = f'{timestamp} - {now} - rates'

    if rules['email']['selected_rates'] is not None:
        tmp = dict()
        for exc in rules['email']['selected_rates']:
            tmp[exc] = rates[exc]
        rates = tmp

    text = json.dumps(rates)

    send_smtp_email(subject, text)


def check_notify_rules(rates):
    """
    check if user defined notify rules and if rates reached to the defined rules, then generate proper msg send.
    :param rates:
    :return: msg(string)
    """
    preferred = rules['notification']['selected_rates']
    msg = ''
    for exc in preferred:
        if rates[exc] <= preferred[exc]['min']:
            msg += f'{exc} reached min:{rates[exc]} \n'
        if rates[exc] >= preferred[exc]['max']:
            msg += f'{exc} reached max:{rates[exc]} \n'
    return msg


def send_notification(msg):
    now = JalaliDatetime(datetime.now()).strftime("%Y-%B-%d %A %H:%M")
    msg += now
    send_sms(msg)


if __name__ == '__main__':
    data = get_rates()

    # if you want to customize, got to config.py
    if rules['archive']:
        archive(data['timestamp'], data['rates'])

    if rules['email']['enable']:
        send_mail(data['timestamp'], data['rates'])

    if rules['notification']['enable']:
        notification_msg = check_notify_rules(data['rates'])
        if notification_msg:
            send_notification(notification_msg)
