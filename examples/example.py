from crypto_pay import CryptoPay

# Your API token from https://t.me/CryptoBot
TOKEN = "TOKEN"

# Instance for CryptoPay
crypto_pay = CryptoPay(TOKEN)


# Call get_me method
try:
    print("get_me")
    me = crypto_pay.get_me()
    print(me)
except Exception as e:
    print(f"Error: {e}")


# Get rates
try:
    print("get_exchange_rates")
    rates = crypto_pay.get_exchange_rates()
    print(rates)
except Exception as e:
    print(f"Error: {e}")
# [{
#         "is_valid": True,
#         "is_crypto": True,
#         "is_fiat": False,
#         "source": "TON",
#         "target": "USD",
#         "rate": "5.69015273",
#     },...]


# Create an invoice
try:
    print("create_invoice")
    invoice = crypto_pay.create_invoice(
        "LTC",
        "1",
        {
            "description": "Payment for services",
            "expires_in": 3600,  # Invoice expires in 1 hour
        },
    )
    print(invoice)
except Exception as e:
    print(f"Error: {e}")


# Check an invoice
try:
    print("get_invoices")
    invoices = crypto_pay.get_invoices()
    print(invoices)
except Exception as e:
    print(f"Error: {e}")
# {'items':
# [
# {
# 'invoice_id': 18266853,
# 'hash': 'IV5G0xPkZzoN',
# 'currency_type': 'crypto',
# 'asset': 'USDC', 'amount': '1',
# 'pay_url': 'https://t.me/CryptoBot?start=IV5G0xPkZzoN',
# 'bot_invoice_url': 'https://t.me/CryptoBot?start=IV5G0xPkZzoN',
# 'mini_app_invoice_url': 'https://t.me/CryptoBot/app?startapp=invoice-IV5G0xPkZzoN',
# 'web_app_invoice_url': 'https://app.send.tg/invoices/IV5G0xPkZzoN',
# 'description': 'Payment for services',
# 'status': 'active',
# 'created_at': '2025-01-06T13:04:51.501Z',
# 'allow_comments': True,
# 'allow_anonymous': True,
# 'expiration_date': '2025-01-06T14:04:51.500Z'
# },
# ]
# }
