from crypto_pay import CryptoPay

# Your API token from https://t.me/CryptoBot
TOKEN = 'YOUR_API_TOKEN'

# Instance for CryptoPay
crypto_pay = CryptoPay(TOKEN)

# Call get_me method
try:
    me = crypto_pay.get_me()
    print(me)
except Exception as e:
    print(f"Error: {e}")

# Create an invoice
try:
    invoice = crypto_pay.create_invoice(CryptoPay.Assets['BTC'], 0.01)
    print(invoice)
except Exception as e:
    print(f"Error: {e}")
    
    from crypto_pay import CryptoPay
