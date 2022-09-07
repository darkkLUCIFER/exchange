# for receiving information about the other rates, you can add them to the end of the url above
url = 'https://api.apilayer.com/fixer/latest?base=USD&symbols=EUR,GBP,TWD,IRR'

API_KEY = 'dwUhVbLZ8xO51usToTqYFfEhLxHkVwcV'

# change rules for your purposes
rules = {
    'archive': True,
    'email': {
        'enable': True,
        'receiver': 'mdn1376@gmail.com',
        'selected_rates': ['EUR', 'IRR']
    },
}
