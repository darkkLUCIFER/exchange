# for receiving information about the other rates, you can add them to the end of the url above
url = 'https://api.apilayer.com/fixer/latest?base=USD&symbols=EUR,GBP,TWD,IRR'

API_KEY = 'dwUhVbLZ8xO51usToTqYFfEhLxHkVwcV'

EMAIL_RECEIVER = 'mdn1376@gmail.com'

# change rules for your purposes
rules = {
    'archive': True,
    'send_mail': True,

    # default selected_rates in None
    # 'selected_rates': None,
    'selected_rates': ['EUR', 'IRR'],
}
