![CryptoPay](media/header.svg)

# Crypto Pay API Python

A Python library for interacting with the Crypto Pay API, allowing you to accept payments in cryptocurrency and manage transactions easily.

Official documentation: https://help.crypt.bot/crypto-pay-api

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Getting Started](#getting-started)
  - [API Methods](#api-methods)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation

You can install the package using `pip`:

```bash
pip install crypto-pay-api-cryptobot
```

## Usage

### Getting Started

To start using the `crypto_pay` library, you first need to create an application and obtain an API token from the Crypto Pay bot. Once you have your token, you can create an instance of the `CryptoPay` class.

```python
from crypto_pay import CryptoPay

# Your API token
TOKEN = 'YOUR_API_TOKEN'

# Create an instance of CryptoPay
crypto_pay = CryptoPay(TOKEN)

# Example: Get app information
try:
    me = crypto_pay.get_me()
    print(me)
except Exception as e:
    print(f"Error: {e}")
```

### API Methods

Here are some of the key methods you can use with the `crypto_pay` library:

#### 1. Get App Information

```python
me = crypto_pay.get_me()
print(me)
```

#### 2. Create an Invoice

You can create a new invoice by specifying the asset and amount:

```python
invoice = crypto_pay.create_invoice('BTC', '0.01', {
    'description': 'Payment for services',
    'expires_in': 3600  # Invoice expires in 1 hour
})
print(invoice)
```

#### 3. Delete an Invoice

To delete an invoice, you need to provide the invoice ID:

```python
result = crypto_pay.delete_invoice(invoice_id)
print(result)  # Should return True on success
```

#### 4. Create a Check

You can create a check that can be activated by a user:

```python
check = crypto_pay.create_check('ETH', '0.05', pin_to_user_id=123456789)
print(check)
```

#### 5. Transfer Coins

To transfer coins from your app's balance to a user, use the transfer method:

```python
transfer_result = crypto_pay.transfer(user_id=123456789, asset='USDT', amount='10.00', spend_id='unique_spend_id')
print(transfer_result)
```

#### 6. Get Invoices

Retrieve a list of invoices created by your app:

```python
invoices = crypto_pay.get_invoices()
print(invoices)
```

#### 7. Get Balance

Get the balance of your app:

```python
balance = crypto_pay.get_balance()
print(balance)
```

#### 8. Get Exchange Rates

Retrieve the exchange rates of supported currencies:

```python
exchange_rates = crypto_pay.get_exchange_rates()
print(exchange_rates)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.