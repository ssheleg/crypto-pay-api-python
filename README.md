![CryptoPay](media/header.svg)

# Crypto Pay API Python

A Python library for interacting with the Crypto Pay API.

Official documentation: https://help.crypt.bot/crypto-pay-api

## Installation

You can install the package using pip:

```bash
pip install crypto-pay-api-cryptobot
```


## Usage
```python
from crypto_pay import CryptoPay

# Your API token
TOKEN = 'YOUR_API_TOKEN'

# Create an instance of CryptoPay
crypto_pay = CryptoPay(TOKEN)

# Example: Get app information
me = crypto_pay.get_me()
print(me)
```