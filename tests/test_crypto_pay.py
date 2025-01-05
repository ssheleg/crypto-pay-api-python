import unittest
from crypto_pay import CryptoPay

class TestCryptoPay(unittest.TestCase):
    
    def setUp(self):
        self.token = 'YOUR_API_TOKEN'  
        self.crypto_pay = CryptoPay(self.token)

    def test_get_me(self):
        response = self.crypto_pay.get_me()
        self.assertIn('ok', response)

    def test_create_invoice(self):
        response = self.crypto_pay.create_invoice('BTC', '0.01')
        self.assertIn('invoice_id', response)

if __name__ == '__main__':
    unittest.main()