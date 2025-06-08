# Exchange  Rates are not updated in real time they are hard coded.
EXCHANGE_RATES = {
    'USD': 1.0,
    'EUR': 0.89,
    'GBP': 0.77,
    'JPY': 110.45,
    'CNY': 6.70,
    'INR': 73.30,
    'RUB': 0.01,
}


def convert(amount, from_currency, to_currency):
    return amount / EXCHANGE_RATES[from_currency] * EXCHANGE_RATES[to_currency]


def take_input():

        from_currency = input('From: ')
        to_currency = input('To: ')
        amount = float(input('Amount: '))
        return amount, from_currency.upper(), to_currency.upper()


def main():
    while True:
        amount, from_currency, to_currency = take_input()
        converted_amount = convert(amount, from_currency, to_currency)
        print(f'{amount} {from_currency} is equal to {converted_amount} {to_currency}')


if __name__ == '__main__':
    main()